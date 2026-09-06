---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-best-practices-for-manufacturing-ot/secure-network-connection-to-local-resources.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Secure network connection to local resources
<a name="secure-network-connection-to-local-resources"></a>

Manufacturing applications running in the AWS Cloud or applications running on an on-premises edge gateway with a connection to the cloud need to access local network resources like PLCs and field devices. These network resources could also include local computers (HMI / SCADA), file systems, or databases. Manufacturing environments often operate under the assumption of implicit trust of the local network resources. Although an edge gateway or agent software could be part of the local network, it should establish connections with other resources in a secure fashion, assuming they are untrusted. Following are some of these best practices.
+  **Use Secure Industrial Protocols** — Historically, Industrial Control Systems (ICSs) have been air-gapped systems (isolated environments), running proprietary control protocols. These ICS protocols have served the challenging needs of the manufacturing industry for decades; however, these protocols were designed assuming all the communications are happening in a trusted environment and hence relied mostly on perimeter security. As a result, ICS protocols didn’t typically support the security requirements for encryption, authentication and authorization.

   But amidst the heightened awareness to industrial cybersecurity and the evolution towards smart factory and cloud connected systems, newer versions of some ICS protocols have been developed to support secure communications. Following are some examples of secure versions of existing industrial protocols.
+  **CIP Security™** — This is a new method of securing the Common Industrial Protocol (CIP) data at the protocol level. CIP is an industrial protocol supported by hundreds of vendors. CIP Security™ adds specifications for authentication, message integrity verification, and encryption to the CIP protocol, making it secure.
+  **Modbus Secure** — This new protocol provides robust protection through the blending of Transport Layer Security (TLS) with the traditional Modbus protocol, a popular industrial protocol. The new protocol leverages X.509 v3 digital certificates for authentication of the server and client. The protocol also supports the transmission of role-based access control information using an X.509 v3 extension to authorize the request of the client.
+  **OPC UA** —Open Process Communications (OPC) is an interoperability standard in the industry. OPC UA is the latest iteration of OPC, which is cross platform and secure by design. It offers a combination of an X.509 certificate and user credential-based authentication and authorization schemes. It also offers data encryption in transit. OPC UA specification also allows for server-initiated connections (reverse connect), which allows clients to communicate with servers without opening any inbound firewall ports.

The best practice is to use the secure versions of protocols. If vendor support is not available, consider upgrading or upfitting the existing control system architecture to enable secure protocol support.
+  **Tighten trust boundaries** — Secure protocols in the ICS world are fairly new, and vendor support for these protocols varies. If upfitting or upgrading to newer protocols is not an option, consider tightening the trust boundary; for example, limiting the scope and area of unsecure communication. One way to tighten the trust boundary is to place a protocol converter that can translate as well as secure the communications as close to the controller (data source) as possible. Protocol converter PLC modules that reside directly in the control panel, can be an option in this case.

Another recommendation is to functionally segregate the plant into multiple cell/area zones (grouping of ICS devices in a functional area like a machine shop, paint booth, or part assembly). In this scenario, the cell/area zone defines the trust boundary where devices are allowed to communicate unhindered and in real time, but traffic leaving or entering the cell/area zone is subject to inspection, as shown in figure 7. Consider using ICS specialized firewall/inspection products that understand the ICS protocols and can detect anomalous behavior in the control network.

![A diagram showing secure connection to local resources.](http://docs.aws.amazon.com/whitepapers/latest/security-best-practices-for-manufacturing-ot/images/secure-conn-local-resources.png)

 *Secure connection to local resources *
