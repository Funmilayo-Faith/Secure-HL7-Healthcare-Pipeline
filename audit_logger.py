from datetime import datetime


def write_log(action, file_name, records, status):
    """
    Writes activity to audit_log.txt
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S"
    )

    log_entry = (
        f"\n{'='*50}\n"
        f"Timestamp : {timestamp}\n"
        f"Action    : {action}\n"
        f"File      : {file_name}\n"
        f"Records   : {records}\n"
        f"Status    : {status}\n"
    )
    
    with open(
        "audit_log.txt",
        "a",
        encoding="utf-8"
    ) as log_file:
        log_file.write(log_entry)