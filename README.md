# BigBank Assignment

## To Do:

## Describe what would be the best practices for a bank to monitor their infrastructure and business.

I think a bank needs to watch two main things: monitoring technical systems and their business processes.

1. Infrastructure monitoring

Banks use many systems: servers, databases, APIs, payment gateways, mobile apps. All of these must work without interruptions.

Some things that should be done:

- Watch important technical indicators (CPU, memory, network, disk, database health).
- Track how fast the website and apps respond and how many errors happen.
- Set alerts so the team gets a message when something is wrong.
- Make dashboards to see the health of the system in one place.
- Check security logs to catch suspicious activities.
- Have a recovery plan if something fails.

2. Business monitoring

Even if the technical systems are fine, the bank also needs to know if customers can actually use the services.

Some things that should be checked:

- If payments and money transfers go through successfully.
- How many transactions fail, and why.
- If certain services are slower than usual.
- Unusual activities.
- Make reports so managers know if the bank is meeting customer expectations.

Why this is important

If a bank checks only the technical side but not the business processes, they might miss real problems for customers

### Sources

1. Atlassian - IT monitoring best practices
https://confluence.atlassian.com/kb/best-practices-for-performance-troubleshooting-tools-652444218.html

2. IBM - Best practices for IT infrastructure monitoring
https://www.ibm.com/think/topics/application-monitoring-best-practices

3. Google SRE Book (Chapter 6)
https://sre.google/sre-book/monitoring-distributed-systems/

## Create simple Python script to monitor external endpoints.

### Requirement:

- Input will be a URL (for example: https://www.delfi.ee/)
- Outputs are:
- Response code
    - Result (if code 200 then OK, else NOK)
    - Response time in ms.

### What have I created?

My script takes a URL, makes a quick request to it, and then:

- Shows the HTTP status code (200 for OK).
- Says if the site is OK or NOK.
- Tells the response time in milliseconds.
- Also exit code can be checked:
    - if the site is working fine - 0
    - if there is a problem - 1

I also decided to use exit codes because in real-world a monitoring system can easily check the 0 or 1 result and decide if there is something that needs an attention.

### How It Works

I use:
- Command-line arguments: to get the URL from the command line.
- Validation: If do not provide exactly one URL, the script will stop and show how to use it.
- Timing: With time.perf_counter() I measure how long the request takes with high accuracy.
- I use the requests library to send the HTTP request, with a 10-second timeout.
- Error handling: A try catch block catches any network errors so the script will not crash.
- Exit codes: return 0 for success and 1 for failure.

### How to Run It

Install requests library
```
pip install requests
```

**Run the script in terminal: (as in the assignment example URL - DELFI)**
```
python assignment.py https://www.delfi.ee/
```
**To check the exit code, is there 0 or 1 in the end:**
```
python assignment.py https://www.delfi.ee/
echo %ERRORLEVEL%
```

#### What else can be done?

If there is result code = 1, it should be good to understand why. So I would add status check in the code, to see what is happening when site is not working.
It should also check if given string is a website or not.