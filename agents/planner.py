def handle(query):
    data = query.replace("plan", "").strip()
    
    if not data:
        return "Planner: Please tell me subjects and hours. \n(Usage example: 'plan math physics 4')"

    try:
        parts = data.split()
        hours = float(parts[-1])      
        subjects = parts[:-1]          

        if not subjects:
            return "Planner: I found the hours, but what subjects?"

        count = len(subjects)
        time_per_subject = hours / count
        
        total_minutes_per_subject = time_per_subject * 60
        pomodoros = int(total_minutes_per_subject / 30) 
        response = f"Planner: Here is your schedule for {hours} hours:\n"
        response += "-" * 40 + "\n"
        
        for subject in subjects:
            response += f"\N{books} **{subject.capitalize()}**: {time_per_subject:.1f} hours\n"
            response += f"   - Focus Blocks: {pomodoros} x (25m work + 5m break)\n"
            response += "\n"
            
        response += "-" * 40 + "\n"
        response += "\N{electric light bulb} Tip: Take a longer 15m break after every 4 block!"
        
        return response

    except ValueError:
        return "Planner: I couldn't understand the numbers. Try: 'plan math physics 4'"