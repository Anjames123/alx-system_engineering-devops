Explanation of the Infrastructure:

1. Additional Servers: By adding two more servers to the infrastructure, we aim to address the single point of failure (SPOF) issue. Having multiple servers allows for redundancy and improved availability.

2. Load Balancer (HAproxy): The load balancer is introduced to distribute incoming requests across the two servers. It helps evenly distribute the traffic and prevents overload on a single server. HAproxy is configured with the Round Robin distribution algorithm, which cyclically sends requests to each server in a sequential order.

3. Active-Passive Setup: The load balancer is configured in an active-passive setup, where only one server actively handles incoming requests while the other server remains idle as a backup. This configuration ensures high availability and failover capability. If the active server fails, the passive server takes over and becomes the new active server.

4. Database Primary-Replica Cluster: The database is set up as a Primary-Replica (Master-Slave) cluster. The primary node, located on Server 1, handles read and write operations, while the replica node, located on Server 2, serves as a read-only copy of the primary node's data.

5. Difference Between Primary and Replica Nodes: The primary node in the database cluster accepts read and write operations, allowing the application to modify and update data. The replica node, on the other hand, serves as a read-only copy of the primary node's data. It replicates the changes made on the primary node and provides read access to the application, enhancing performance and scalability.

Issues with the Infrastructure:

1. Single Point of Failure (SPOF): The load balancer remains a single point of failure in this infrastructure. If the load balancer fails, it would disrupt the distribution of requests and result in service unavailability.

2. Security Issues: The infrastructure lacks a firewall and does not utilize HTTPS (HTTP Secure). This leaves the system vulnerable to potential security threats and attacks, compromising the confidentiality and integrity of user data.

3. No Monitoring: Without proper monitoring tools and practices in place, it becomes challenging to identify and address performance issues, resource utilization, and potential failures effectively. Monitoring is crucial for maintaining and optimizing the web infrastructure.
