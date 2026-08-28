---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/ad-connector-cannot-connect-to-active-directory.html
---

# AD Connector cannot connect to Active Directory
<a name="ad-connector-cannot-connect-to-active-directory"></a>

 For AD Connector to connect to the on-premises directory, the firewall for the on-premises network must have certain ports open to the CIDRs for both subnets in the VPC. Refer to [Scenario 1: Using AD Connector to Proxy Authentication to On-Premises Active Directory Service](scenario-1-using-ad-connector-to-proxy-authentication-to-on-premises-active-directory-service.md). To test if these conditions are met, perform the following steps.

 **To test the connection:**

1.  Launch a Windows instance in the VPC and connect to it over RDP. The remaining steps are performed on the VPC instance.

1.  Download and unzip the [DirectoryServicePortTest](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/samples/DirectoryServicePortTest.zip) test application. The source code and Microsoft Visual Studio project files are included to modify the test application, if desired.

1.  From a Windows command prompt, run the DirectoryServicePortTest test application with the following options:

```
DirectoryServicePortTest.exe -d <domain_name>
-ip <server_IP_address> -tcp "53,88,135,139,389,445,464,636,49152" -udp "53,88,123,137,138,389,445,464" <domain_name>
```

 *<domain\_name>* — The fully qualified domain name, used to test the forest and domain functional levels. If the domain name is excluded, the functional levels won't be tested.

 <*server\_IP\_address>* — The IP address of a domain controller in the on-premises domain. The ports are tested against this IP address. If the IP address is excluded, the ports won't be tested.

 This test determines if the necessary ports are open from the VPC to the domain. The test app also verifies the minimum forest and domain functional levels.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
