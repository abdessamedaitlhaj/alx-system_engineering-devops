## Postmortem
### Issue Summary
The outage started today at 8 AM (UTC + 1) and was fixed and ended at 10 AM (UTC + 1). The outage takes the server down which leads to inaccessible services or content in the server and the users will not get the issue same as technical team, so they will have bad experience, and 100% that willing to interact with the server in the meantime will receive an error. The root cause is that the server receives too many requests in a short time.
### Timeline
+ 11:00 AM UTC: The outage was detected one hour after it’s ended.
+ 11:30 AM UTC: The team was able to find and notice the issue from customers complaining about messages received via emails saying that they are not able to access the web site of our application.
+ 12:00 AM UTC: The team investigate and check our servers for potential errors that caused the problem, they check the logs area and find out that servers deal with a lot of requests in specific duration of time which crash our server.
+ 11:45 AM UTC: Firstly after the team noticed the error they inspected some settings and configuration files, database connection issues.
+ 12:10 PM UTC: Once the incident was found then it was escalated to our software engineering team to take the appropriate actions.
+ 12:30 PM UTC: They increase our server capacity by adding more resources such as additional servers, CPU, memory and implementing a load balancing solution to distribute incoming traffic across multiple servers.
### Root cause and resolution
The issue is related to a server crash due to a huge amount of traffic received in a particular duration of time, the server was not able to handle all requests it’s out of the usual routine, so we successfully find out what caused the outage and duplicate our server and implement a load balanced in order to avoid overwhelmed server.
### Corrective and preventative measures
Generally if it is possible to feed the application to multiple servers and more numbers means safety to avoid such issues. We are capable of addressing this issue like this : Get more servers, configure them (nginx, load balancing …), add monitoring service.

