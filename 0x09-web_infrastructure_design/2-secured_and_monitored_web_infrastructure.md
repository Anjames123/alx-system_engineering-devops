Explanation of the Infrastructure:

1. Additional Firewalls: Three firewalls are added to the infrastructure to enhance security. Firewalls act as a barrier between the external network (Internet) and the internal servers, filtering and controlling incoming and outgoing network traffic based on predetermined security rules. They help protect the web infrastructure from unauthorized access, malicious attacks, and potential vulnerabilities.

2. SSL Certificate and HTTPS: The load balancer is configured to terminate SSL, meaning it decrypts the HTTPS traffic from users and forwards it as plain HTTP to the servers. To secure the website, an SSL certificate is added, allowing the traffic to be served over HTTPS. HTTPS encrypts the communication between the user's browser and the web server, ensuring confidentiality, integrity, and authentication of data transmitted over the network.

3. Monitoring Clients (Data Collectors): Three monitoring clients are deployed to collect data and send it to a monitoring service such as Sumo Logic. Monitoring clients are responsible for gathering metrics, logs, and performance data from the servers, web servers, and application components. They provide insights into the health, performance, and availability of the web infrastructure, allowing proactive identification and resolution of issues.

4. Monitoring Purpose: Monitoring is used to track and analyze the performance, availability, and health of the web infrastructure. It helps identify potential problems, such as high response times, errors, resource usage, and network issues. Monitoring enables proactive maintenance, troubleshooting, and optimization of the infrastructure to ensure optimal user experience and minimize downtime.

5. Data Collection by Monitoring Tool: The monitoring tool collects data by installing agents or clients on the servers, which gather relevant metrics, logs, and performance data. These agents communicate with the monitoring service, sending the collected data for analysis and visualization in real-time or through periodic intervals.

6. Monitoring Web Server QPS: To monitor the web server's QPS (Queries Per Second), the monitoring tool can collect metrics related to incoming HTTP requests, track the number of requests per second, and analyze trends over time. By setting up appropriate monitoring thresholds, alerts can be triggered when the QPS exceeds predefined limits, enabling proactive scaling or optimization measures.

Issues with the Infrastructure:

1. Terminating SSL at the Load Balancer Level: Terminating SSL at the load balancer level can be an issue if the communication between the load balancer and the application servers is not secured. It introduces a potential vulnerability as the traffic between the load balancer and the application servers is transmitted as plain HTTP, leaving it susceptible to eavesdropping or unauthorized access. Encrypting the communication between the load balancer and the application servers is recommended to ensure end-to-end security.

2. Single MySQL Server Capable of Accepting Writes: Having only one MySQL server capable of accepting write operations creates a single point of failure. If the primary node fails, write operations cannot be performed until the primary node is restored. This can lead to service disruption and potential data loss. Implementing a highly available database setup, such as a multi-master or master-master replication, can mitigate this issue.

3. Servers with All the Same Components: Having servers with identical components (database, web server, and application server) can lead to potential issues related to scalability, performance, and maintenance. For example, if the application server or database server becomes a bottleneck, it affects all servers since they are configured identically. Introducing different server roles, such as separating database servers from application servers, can provide more flexibility in scaling, optimizing performance, and managing resources effectively.
