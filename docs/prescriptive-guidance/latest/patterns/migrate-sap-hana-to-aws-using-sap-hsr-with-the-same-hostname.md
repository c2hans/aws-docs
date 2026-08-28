---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-sap-hana-to-aws-using-sap-hsr-with-the-same-hostname.html
---

# Migrate SAP HANA to AWS using SAP HSR with the same hostname
<a name="migrate-sap-hana-to-aws-using-sap-hsr-with-the-same-hostname"></a>

*Pradeep Puliyampatta, Amazon Web Services*

## Summary
<a name="migrate-sap-hana-to-aws-using-sap-hsr-with-the-same-hostname-summary"></a>

SAP HANA migrations to Amazon Web Services (AWS) can be performed using multiple options, including backup and restore, export and import, and SAP HANA System Replication (HSR). The selection of a particular option depends on the network connectivity between source and target SAP HANA databases, the size of the source database, downtime considerations, and other factors.

The SAP HSR option for migrating SAP HANA workloads to AWS works well when there is a stable network between the source and target systems and the entire database (SAP HANA DB replication snapshot) can be completely replicated within 1 day, as stipulated by SAP for network throughput requirements for SAP HSR. The downtime requirements with this approach are limited to performing the takeover on the target AWS environment, SAP HANA DB backup, and post-migration tasks.

SAP HSR supports the use of different hostnames (hostnames mapped to different IP addresses) for replication traffic between the primary, or source, and secondary, or target, systems. You can do this by defining those specific sets of hostnames under the `[system_replication_hostname_resolution]` section in `global.ini`. In this section, all hosts of the primary and the secondary sites must be defined on each host. For detailed configuration steps, see the [SAP documentation](https://help.sap.com/viewer/eb3777d5495d46c5b2fa773206bbfb46/1.0.12/en-US/c0cba1cb2ba34ec89f45b48b2157ec7b.html).

One key takeaway from this setup is that the hostnames in the primary system must be different from the hostnames in the secondary system. Otherwise, the following errors can be observed.
+ `"each site must have a unique set of logical hostnames"`
+ `"remoteHost does not match with any host of the source site. All hosts of source and target site must be able to resolve all hostnames of both sites correctly"`

However, the number of post-migration steps can be reduced by using the same SAP HANA DB hostname on the target AWS environment.

This pattern provides a workaround for using the same hostname on source and target environments when using the SAP HSR option. With this pattern, you can use the SAP HANA Hostname Rename option. You assign a temporary hostname to the target SAP HANA DB to facilitate hostname uniqueness for SAP HSR. After the migration completes the takeover milestone on the target SAP HANA environment, you can revert the target system hostname back to the hostname of the source system.

## Prerequisites and limitations
<a name="migrate-sap-hana-to-aws-using-sap-hsr-with-the-same-hostname-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ A virtual private cloud (VPC) with a virtual private network (VPN) endpoint or a router.
+ AWS Client VPN or AWS Direct Connect configured to transfer files from the source to the target.
+ SAP HANA databases in both the source and the target environment. The target SAP HANA DB patch level should be equal to or higher than the source SAP HANA DB patch level, within the same SAP HANA Platform edition. For example, replication cannot be set up between HANA 1.0 and HANA 2.0 systems. For more information, see question 15 in SAP Note: 1999880 – FAQ: SAP HANA System Replication.
+ SAP application servers in the target environment.
+ Amazon Elastic Block Store (Amazon EBS) volumes in the target environment.

**Limitations**

The following list of SAP documents covers known issues that are related to this workaround, including constraints regarding SAP HANA dynamic tiering and scale-out migrations:
+ 2956397 – Renaming of SAP HANA Database System failed
+ 2222694 – When trying to rename the HANA system, the following error appears "Source files are not owned by the original sidadm user (uid = xxxx)"
+ 2607227 – hdblcm: register\_rename\_system: Renaming SAP HANA instance failed
+ 2630562 – HANA Hostname Rename failed and HANA does not start up
+ 2935639 – sr\_register is not using the hostname that is specified under system\_replication\_hostname\_resolution in the global.ini section
+ 2710211 – Error: source system and target system have overlapping logical hostnames
+ 2693441 – Failed to rename an SAP HANA System due to error
+ 2519672 – HANA Primary and Secondary has different system PKI SSFS data and key or unable to check
+ 2457129 – SAP HANA System Host Rename is not Permitted when Dynamic Tiering is Part of Landscape
+ 2473002 – Using HANA System Replication to migrate scale out system (There are no restrictions provided by SAP in using this hostname rename approach for scale-out SAP HANA systems. However, the procedure must be repeated on each individual host. Other scale-out migration limitations also apply to this approach.)

**Product versions**
+ This solution applies to SAP HANA DB platform edition 1.0 and 2.0.

## Architecture
<a name="migrate-sap-hana-to-aws-using-sap-hsr-with-the-same-hostname-architecture"></a>

**Source setup**

An SAP HANA database is installed on the source environment. All the SAP application server connections and DB interfaces use the same hostname for client connections. The following diagram shows the example source hostname `hdbhost` and its corresponding IP address.

![SAP HANA DB source hdbhost in a corporate data center with IP address 10.1.2.1.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/004781c1-96df-43dd-a52e-ed1db5bdf9ef/images/a1b28c3a-93b7-4f82-a5da-81008b74c9ae.png)

**Target setup**

The AWS Cloud target environment uses the same hostname to run an SAP HANA database. The target environment on AWS includes the following:
+ SAP HANA database
+ SAP application servers
+ EBS volumes

![SAP HANA DB target hdbhost in the AWS Cloud with IP address 172.16.2.1.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/004781c1-96df-43dd-a52e-ed1db5bdf9ef/images/7f45d7aa-9b80-4413-bec9-1616492b650c.png)

**Intermediate configuration**

In the following diagram, the hostname on the AWS target environment is temporarily renamed as `temp-host` so that the hostnames on the source and target are unique. After the migration completes the takeover milestone on the target environment, the target system virtual hostname is renamed using the original name, `hdbhost`.

The intermediate configuration includes one of the following options:
+ AWS Client VPN with a Client VPN endpoint
+ Direct Connect connecting to a router

![Source system to target AWS Cloud system with temp-host IP address 172.31.5.10.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/004781c1-96df-43dd-a52e-ed1db5bdf9ef/images/e2794477-2e8f-4974-bca3-2275f6809fce.png)

SAP application servers on the AWS target environment can be installed either before replication setup or after the takeover. However, installing the application servers before replication setup can help with reduction of downtime during installation, configuration of high availability, and backups.

## Tools
<a name="migrate-sap-hana-to-aws-using-sap-hsr-with-the-same-hostname-tools"></a>

**AWS services**
+ [AWS Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/client-vpn-user-what-is.html) is a managed client-based VPN service that enables you to securely access AWS resources and resources in your on-premises network.
+ [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) links your internal network to an Direct Connect location over a standard Ethernet fiber-optic cable. With this connection, you can create virtual interfaces directly to public AWS services, bypassing internet service providers in your network path.
+ [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html) provides block level storage volumes for use with Amazon Elastic Compute Cloud (Amazon EC2) instances. EBS volumes behave like raw, unformatted block devices. You can mount these volumes as devices on your instances.

**Other tools**
+ [SAP application servers](https://help.sap.com/doc/saphelp_nw73ehp1/7.31.19/en-US/47/a032c0305e0b3ae10000000a42189d/content.htm?no_cache=true) – SAP application servers provide programmers with a way to express business logic. The SAP application server performs the data processing based on the business logic. The actual data is stored in a database, which is a separate component.
+ [SAP HANA cockpit](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/2.0.03/en-US/da25cad976064dc0a24a1b0ee9b62525.html) and [SAP HANA Studio](https://help.sap.com/viewer/a2a49126a5c546a9864aae22c05c3d0e/2.0.00/en-US/c831c3bbbb571014901199718bf7edc5.html) – Both SAP HANA cockpit and SAP HANA Studio provide an administrative interface to the SAP HANA database. In SAP HANA Studio, the SAP HANA Administration console is the system view that provides relevant content for SAP HANA database administration.
+ [SAP HANA System Replication](https://help.sap.com/viewer/4e9b18c116aa42fc84c7dbfd02111aba/2.0.04/en-US) – SAP HANA System Replication (SAP HSR) is the standard procedure provided by SAP for replicating SAP HANA databases. The required executables for SAP HSR are part of the SAP HANA server kernel itself.

## Epics
<a name="migrate-sap-hana-to-aws-using-sap-hsr-with-the-same-hostname-epics"></a>

### Prepare the source and target environments
<a name="prepare-the-source-and-target-environments"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install and configure the SAP HANA databases. | In the source and target environments, ensure that the SAP HANA DB is installed and configured according to SAP HANA on best practices. For more information, see [SAP HANA on AWS](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana.pdf). | SAP Basis administration |
| Map the IP address. | In the target environment, ensure that the temporary hostname is assigned to an internal IP address. 1. Assign a secondary IPv4 address to the EC2 instance on the AWS Management Console by navigating to **EC2**, **Instance**, **Actions**, **Networking**, **Manage IP address**, **Assign new IP address**. <br />2. To assign the same address to the EC2 network adaptor (NIC), from the operating system, as root user, run the command `ip addr add <IP>/32 dev eth0`, replacing `<IP>` with the IP address from step 1. | AWS administration |
| Resolve target hostnames. | On the secondary SAP HANA DB, confirm that both hostnames (`hdbhost` and `temp-host`) are resolved for the SAP HANA replication networks by updating the relevant hostnames in the `/etc/hosts` file. | Linux administration |
| Back up the source and target SAP HANA databases. | Use SAP HANA Studio or the SAP HANA cockpit to perform backups on the SAP HANA databases. | SAP Basis administration |
| Exchange system PKI certificates. | (Applies only to SAP HANA 2.0 and later) Exchange certificates in the system public key infrastructure (PKI) secure store in the file system (SSFS) store between the primary and secondary databases. For more information, see SAP Note 2369981 – Required configuration steps for authentication with SAP HANA System Replication. | SAP Basis administration |

### Rename the target SAP HANA DB
<a name="rename-the-target-sap-hana-db"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Stop target client connections. | In the target environment, shut down the SAP application servers and other client connections. | SAP Basis administration |
| Rename the target SAP HANA DB to the temporary hostname. | 1. As root user, rename the target SAP HANA DB hostname to the temporary hostname by using resident `hdblcm`. <pre>root $> cd /hana/shared/<SID/hdblcm<br />root $> ./hdblcm</pre><br />2. Choose option `9 \| rename_system \| Rename the SAP HANA Database System`.<br />3. Provide the new name:` temp-host`.<br />4. You can validate other options as needed. However, be sure that you don’t mix up the host rename with a SID change (SAP Note 2598814 – hdblcm: SID rename fails).The SAP HANA DB stop and start will be controlled by `hdblcm`.  | SAP Basis administration |
| Assign replication networks. | In the `global.ini` file of the source system, under the `[system_replication_hostname_resolution]` header, provide the source and target replication network details. Then copy the entries to the `global.ini` file on the target system. | SAP Basis administration |
| Enable replication on primary. | To enable replication on the source SAP HANA DB, run the following command. <pre>hdbnsutil -sr_enable --name=siteA</pre> | SAP Basis administration |
| Register the target SAP HANA DB as a secondary system. | To register the target SAP HANA DB as a secondary system to source for SAP HSR, choose **async** replication. <pre>(sid)adm $> HDB stop<br />(sid)adm $> hdbnsutil -sr_register –name=siteB –remotehost=hdbhost /<br />--remoteInstance=00 –replicationMode=async –operationMode=logreplay<br />(sid)adm $> HDB start</pre><br />Alternatively, you can choose the `–online` option to register. In that case, you don’t need to stop and start the SAP HANA DB. | SAP Basis administration |
| Validate synchronization. | On the source SAP HANA DB, verify that all the logs are applied on the target system (because it is async replication).<br />To verify the replication, on the source, run the following commands.<pre>(sid)adm $> cdpy<br />(sidadm $> python systemReplicationStatus.py</pre> | SAP Basis administration |
| Shut down the source SAP application and SAP HANA DB. | During the migration cutover, perform a shutdown of the source system (the SAP application and SAP HANA database. | SAP Basis administration |
| Perform a takeover at the target. | To perform a takeover at the target on AWS, run the command `hdbnsutil -sr_takeover`. | SAP Basis administration |
| On the target SAP HANA DB, turn off replication. | To clear the replication metadata, stop replication on the target system by running the command `hdbnsutil -sr_disable`. This is in accordance with SAP Note 2693441 – Failed to rename an SAP HANA System due to error. | SAP Basis administration |
| Back up the target SAP HANA DB. | After the takeover is successful, we recommend performing a full SAP HANA DB backup. | SAP Basis administration |

### Revert to the original hostname in the target system
<a name="revert-to-the-original-hostname-in-the-target-system"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Revert the target SAP HANA DB hostname to the original. | 1. To revert the target SAP HANA DB hostname to the original virtual hostname, use resident `hdblcm`. <pre>root $> cd /hana/shared/<SID>/hdblcm<br />root $> ./hdblcm</pre><br />2. Choose option `9 \| rename_system \| Rename the SAP HANA Database System`.<br />3. Provide the new name: `hdbhost`.You can validate other options as needed. However, be sure that you don’t mix up the host rename with a SID change (SAP Note 2598814 – hdblcm: SID rename fails). | SAP Basis administration |
| Adjust hdbuserstore. | Adapt the `hdbuserstore` details pointing to the source `schema/user` details. For detailed steps, see the [SAP documentation](https://help.sap.com/viewer/b3ee5778bc2e4a089d3299b82ec762a7/2.0.02/en-US/ddbdd66b632d4fe7b3c2e0e6e341e222.html?q=hdbuserstore). <br />To validate this step, run the command `R3trans -d`. The result should reflect a successful connection to the SAP HANA database. | SAP Basis administration |
| Start up client connections. | In the target environment, start up the SAP application servers and other client connections. | SAP Basis administration |

## Related resources
<a name="migrate-sap-hana-to-aws-using-sap-hsr-with-the-same-hostname-resources"></a>

**SAP references**

SAP documentation references are frequently updated by SAP. To stay up to date, see SAP Note 2407186 – How-To Guides & Whitepapers For SAP HANA High Availability.

*Additional SAP notes*
+ 2550327 – How-To Rename an SAP HANA System
+ 1999880 – FAQ: SAP HANA System Replication
+ 2078425 – Troubleshooting note for SAP HANA platform lifecycle management tool hdblcm
+ 2592227 – FQDN suffix change in HANA systems
+ 2048681 – Performing SAP HANA platform lifecycle management administration tasks on multiple-host systems without SSH or root credentials

*SAP documents*
+ [System Replication Network Connection](https://help.sap.com/docs/SAP_HANA_PLATFORM/4e9b18c116aa42fc84c7dbfd02111aba/47190b425eb1433697b026ecd46ff5f9.html)
+ [Host Name Resolution for System Replication](https://help.sap.com/viewer/eb3777d5495d46c5b2fa773206bbfb46/1.0.12/en-US/c0cba1cb2ba34ec89f45b48b2157ec7b.html)

**AWS references**
+ [Migrating SAP HANA from Other Platforms to AWS](https://docs.aws.amazon.com/sap/latest/sap-hana/migrating-hana-hana-to-aws.html)

## Additional information
<a name="migrate-sap-hana-to-aws-using-sap-hsr-with-the-same-hostname-additional"></a>

The changes performed by `hdblcm` as part of the hostname rename activity are consolidated in the following verbose log.

![Code showing processes stopped on temp-host, starting on hdbhost, and SAP HANA DB system renamed.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/004781c1-96df-43dd-a52e-ed1db5bdf9ef/images/9e0c11ca-6555-484f-9639-107f60f725f5.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
