def unique_name_collector_until_done():
    unique_names = {}
    
    print("Enter names one by one (type 'done' to finish):")
    
    while True:
        name = input(f"Enter name #{len(unique_names) + 1} (or 'done' to stop): ").strip()
        
        if name.lower() == 'done':
            if len(unique_names) == 0:
                print("No names collected. Exiting.")
                return []
            break
            
        if not name:
            print("Name cannot be empty. Please try again.")
            continue
            
        name_lower = name.lower()
        
        if name_lower in unique_names:
            print(f"'{name}' is a duplicate of '{unique_names[name_lower]}'. Please enter a different name.")
        else:
            unique_names[name_lower] = name
            print(f"✓ '{name}' added. Total unique names: {len(unique_names)}")
    
    return list(unique_names.values())

# Run it
collected = unique_name_collector_until_done()
print(f"\nFinal collection ({len(collected)} names): {collected}")