import sys
import csv

def format_field(value, position, total_fields, skipQuote):
    """
    Format the field based on its position and content.
    - Apply double quotes unless it's the first, last, or second last field, or if the field is empty.
    - Add a comma at the end if total_fields is 5.
    """
    if skipQuote or not value:
        formatted_value = value  # No quotes for the first, last, or second last fields, or if the value is empty
    else:
        formatted_value = f'"{value}"'  # Manually add quotes for specific fields

    # Add a comma at the end if total_fields is 5
    # if position == 6 and value == "":
    #     formatted_value += ","
    

    return formatted_value


def main():
    # Read all lines from stdin
    input_lines = sys.stdin.read().splitlines()
    
    # Parse CSV records
    records = []
    for line in input_lines:
        if not line.strip():
            continue  # Skip empty lines
        reader = csv.reader([line], quotechar='"', doublequote=False)
        fields = next(reader)
        if len(fields) != 6:
            continue
        event_id = fields[0]
        event_title = fields[1]
        acronym = fields[2]
        project_code = fields[3]
        project_code_3d = fields[4]
        record_type = fields[5]
        record = {
            'Event ID': event_id,
            'Event Title': event_title,
            'Acronym': acronym,
            'Project Code': project_code,
            '3 Digit Project Code': project_code_3d,
            'Record Type': record_type
        }
        records.append(record)

    # Exclude records with no acronym
    records = [r for r in records if r['Acronym']]

    # Build a mapping from Acronym to events
    acronym_events = {}
    for r in records:
        acronym = r['Acronym']
        if acronym not in acronym_events:
            acronym_events[acronym] = []
        acronym_events[acronym].append(r)

    # Process each Acronym
    output_sets = []
    for acronym in sorted(acronym_events.keys()):
        events = acronym_events[acronym]
        parents = [e for e in events if e['Record Type'] == 'Parent Event']
        children = [e for e in events if e['Record Type'] == 'IEEE Event']

        if len(parents) != 1 or len(children) == 0:
            continue

        parent_event = parents[0]
        child_project_codes_3d = set(e['3 Digit Project Code'] for e in children)
        if len(child_project_codes_3d) == 1:
            parent_event['3 Digit Project Code'] = child_project_codes_3d.pop()
        else:
            parent_event['3 Digit Project Code'] = '???'

        for child in children:
            child['Parent ID'] = parent_event['Event ID']

        children.sort(key=lambda x: (x['Event Title'], x['Event ID']))

        output_set = [parent_event] + children
        output_sets.append(output_set)

    # Output manually without using csv.writer to control quotes and format
    for output_set in output_sets:
        for record in output_set:
            fields = [
                format_field(record.get('Event ID', ''), 0, len(record), True),
                format_field(record.get('Event Title', ''), 1, len(record), False),
                format_field(record.get('Acronym', ''), 2, len(record), False),
                format_field(record.get('Project Code', ''), 3, len(record), True),
                format_field(record.get('3 Digit Project Code', ''), 4, len(record), True),
                format_field(record.get('Record Type', ''), 5, len(record), False),
                format_field(record.get('Parent ID', ''), 6, len(record), True) if 'Parent ID' in record else ''
            ]
            
            pp = ",".join(fields)
            pp = pp.rstrip(',')
            print(pp)

if __name__ == "__main__":
    main()
