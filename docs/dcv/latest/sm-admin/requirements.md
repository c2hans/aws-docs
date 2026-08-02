---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-admin/requirements.html
---

# Amazon DCV Session Manager requirements
<a name="requirements"></a>

The Amazon DCV Session Manager Agent and Broker have the following requirements.

|  | Broker | Agent |
| --- | --- | --- |
| **Operating system** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/dcv/latest/sm-admin/requirements.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/dcv/latest/sm-admin/requirements.html)  |
| **Architecture** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/dcv/latest/sm-admin/requirements.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/dcv/latest/sm-admin/requirements.html)  |
| **Memory** | 8 GB | 4 GB |
| **Amazon DCV version** | Amazon DCV 2020.2 and later | Amazon DCV 2020.2 and later |
| **Additional requirements** | Java 11 |  -  |

## Networking and connectivity requirements
<a name="network-reqs"></a>

The following diagram provides a high-level overview of the Session Manager networking and connectivity requirements.

![Amazon DCV Session Manager network architecture](http://docs.aws.amazon.com/dcv/latest/sm-admin/images/requirements.png)

The **Broker** must be installed on a separate host, but it must have network connectivity with the Agents on the Amazon DCV servers. If you choose to have multiple Brokers to improve availability, then you must install and configure each broker on a separate host, and use one or more load balancers to manage the traffic between the client and the Brokers, and the Brokers and the Agents. The Brokers should also be able to communicate with each other in order to exchange information about the Amazon DCV servers and sessions. The Brokers can store their keys and status data on an external database and have this information available after reboot or termination. This helps mitigate the risk of losing important Broker information by persisting it on the external database. You can retrieve it later. If you choose to have it, then you must set up the external database and configure the brokers. DynamoDB, MariaDB, and MySQL are supported. You can find configuration parameters are listed on the [Broker Configuration File](https://docs.aws.amazon.com/dcv/latest/sm-admin/broker-file.html).

The **Agents** must be able to initiate secure, persistent, bi-directional HTTPs connections with the Broker.

Your **client**, or frontend application, must be able to access the Broker in order to call the APIs. The client should also be able to access your authentication server.
