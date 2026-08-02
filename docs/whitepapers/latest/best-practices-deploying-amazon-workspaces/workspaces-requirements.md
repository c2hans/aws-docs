---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/workspaces-requirements.html
---

# WorkSpaces requirements
<a name="workspaces-requirements"></a>

 The Amazon WorkSpaces service requires three components to deploy successfully:
+  **WorkSpaces client application** — An Amazon WorkSpaces-supported client device. Refer to [Getting Started with Your WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/client_help.html#client_list).

   You can also use Personal Computer over Internet Protocol (PCoIP) Zero Clients to connect to WorkSpaces. For a list of available devices, refer to [PCoIP Zero Clients for Amazon WorkSpaces](https://www.teradici.com/product-service-finder/pcoip-zero-clients).
+  **A directory service to authenticate users and provide access to their WorkSpace** — Amazon WorkSpaces currently works with [AWS Directory Service](https://aws.amazon.com/directoryservice/) and Microsoft AD. You can use your on-premises AD server with AWS Directory Service to support your existing enterprise user credentials with Amazon WorkSpaces.
+  **Amazon Virtual Private Cloud (Amazon VPC) in which to run your Amazon WorkSpaces** — You’ll need a minimum of two subnets for an Amazon WorkSpaces deployment because each AWS Directory Service construct requires two subnets in a multi-AZ deployment.
