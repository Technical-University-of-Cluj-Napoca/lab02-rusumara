import os
from datetime import datetime

def smart_log(*args, **kwargs) -> None:
    level = kwargs.get("level", "info").lower()
    timestamp = kwargs.get("timestamp", False)
    date = kwargs.get("date", False)
    save_to = kwargs.get("save_to", None)
    colored = kwargs.get("color", True)
    
    message = " ".join(str(arg) for arg in args)
    
    colors = {
        "info": "\033[94m",     # Blue
        "debug": "\033[90m",    # Gray
        "warning": "\033[93m",  # Yellow
        "error": "\033[91m"     # Red
    }
    reset = "\033[0m"
    
    now = datetime.now()
    prefix_parts = []
    if date:
        prefix_parts.append(now.strftime("%Y-%m-%d"))
    if timestamp:
        prefix_parts.append(now.strftime("%H:%M:%S"))
    prefix = " ".join(prefix_parts)
    if prefix:
        prefix += " "
    
    log_line = f"{prefix}[{level.upper()}] {message}"
    
    if colored and level in colors:
        log_line = f"{colors[level]}{log_line}{reset}"
    
    print(log_line)
    
    if save_to:
        os.makedirs(os.path.dirname(save_to), exist_ok=True)
        with open(save_to, "a", encoding="utf-8") as f:
            clean_line = f"{prefix}[{level.upper()}] {message}\n"
            f.write(clean_line)
if __name__ == "__main__":
    smart_log("This is an info message.", level="info", timestamp=True, date=True, save_to="logs/app.log")
    smart_log("This is a debug message.", level="debug", timestamp=True)
    smart_log("This is a warning message.", level="warning", date=True)
    smart_log("This is an error message.", level="error", color=False)
    