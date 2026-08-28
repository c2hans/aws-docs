---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/videocalling-networking-requirements.html
---

# Agent workstation requirements for app, web, and video calling in Connect Customer
<a name="videocalling-networking-requirements"></a>

The Connect Customer in-app, web, and video calling capabilities enable your customers to contact you without ever leaving your web or mobile application. The video calling capabilities use the Amazon Chime SDK communication primitives for the video stream. The voice experience is handled through Connect Customer.

**Important**
Video calling does not support VDI environments.

The following table shows the additional networking requirements for your agents' workstation.

| Domain | Subnet | Ports |
| --- | --- | --- |
| \*.chime.aws | 99.77.128.0/18  | 443 (TCP)<br />3478 (UDP) |

The following diagram shows the networking requirements for the customers who are using the communications widgets to contact you.

![The networking requirements for customers using web calling or video.](http://docs.aws.amazon.com/connect/latest/adminguide/images/networking-customer.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
