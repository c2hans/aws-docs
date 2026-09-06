---
source_url: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/security-groups.html
---

Version 4 (V4) of the AWS SDK for .NET has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html)

# Working with security groups in Amazon EC2
<a name="security-groups"></a>

In Amazon EC2, a *security group* acts as a virtual firewall that controls the network traffic for one or more EC2 instances. By default, EC2 associates your instances with a security group that allows no inbound traffic. You can create a security group that allows your EC2 instances to accept certain traffic. For example, if you need to connect to an EC2 Windows instance, you must configure the security group to allow RDP traffic.

To read more about security groups see [Amazon EC2 security groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html) in the [Amazon EC2 User Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/).

**Warning**
EC2-Classic was retired on August 15, 2022. We recommend that you migrate from EC2-Classic to a VPC. For more information, see the blog post [EC2-Classic Networking is Retiring – Here's How to Prepare](https://aws.amazon.com/blogs/aws/ec2-classic-is-retiring-heres-how-to-prepare/).

For information about the APIs and prerequisites, see the parent section ([Working with Amazon EC2](ec2-apis-intro.md)).

**Topics**
+ [Enumerating security groups](enumerate-security-groups.md)
+ [Creating security groups](creating-security-group.md)
+ [Updating security groups](authorize-ingress.md)
