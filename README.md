# Date Assistance Tool

## Overview
Date Assistance Tool is a Python project designed to help with date-related operations. This tool provides various functionalities to manipulate and format dates efficiently.
Mostly related to share a valid calendar-based invite for tools that doesn't have any similar tool such as Whastapp, Telegram, Discord, etc.

## Features
- Date formatting
- Date calculations
- Date parsing

## Usage
- Git clone the repo to destined directory.
- Optional, I'd rather use python virtual environment.
- To install the necessary dependencies, run:

```bash
pip install -r requirements.txt
```
- run the script:
```python
python main.py
```
## Expected output

### Example:

Please enter the event details:

Enter the name of the event: SOC event<br>
Enter the date of the event (YYYY-MM-DD): 2024-09-24<br>
Enter the time of the event (HH:MM AM/PM): 06:30 PM<br>
Enter the origin country code (e.g., CO for Colombia): CO<br>

Event Details:<br>
  Event name: SOC event<br>
  Original country (CO), date and time: 2024-09-24 06:30 PM -05

Converted Times:<br>
  05:30 PM | 🇨🇷, 🇬🇹, 🇭🇳, 🇸🇻<br>
  06:30 PM | 🇨🇴, 🇵🇦, 🇵🇪<br>
  07:30 PM | 🇩🇴, 🇵🇷, 🇵🇾, 🇻🇪<br>
  08:30 PM | 🇦🇷, 🇺🇾<br>

## Contributing
Guidelines for contributing to the project.

- Fork the repository.
- Create a new branch (git checkout -b feature-branch).
- Make your changes.
- Commit your changes (git commit -m 'Add some feature').
- Push to the branch (git push origin feature-branch).
- Open a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.