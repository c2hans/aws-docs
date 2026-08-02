---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/imdsv2.html
---

# IMDSv2
<a name="imdsv2"></a>

By default, any instances launched with the AL2023 AMI require IMDSv2-only and your default hop limit will be set to 2 to allow for containerized workload support. This is done by setting the `imds-support` parameter to `v2.0`. For more information, see [Configure the AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#configure-IMDS-new-instances-ami-configuration) in the *Amazon EC2 User Guide*.

**Note**
The session token's time of validity can be anywhere between 1 second and 6 hours. The addresses to direct the API requests for IMDSv2 queries are the following:
IPv4: 169.254.169.254
IPv6: fd00:ec2::254

You can manually override these settings and enable IMDSv1 using Instance Metadata option launch properties. You can also use IAM controls to enforce different IMDS settings. For more information about setting up and using the Instance Metadata Service, see [Use IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service), [Configure instance metadata options for new instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances), and [Modify instance metadata options for existing instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-existing-instances), in the *Amazon EC2 User Guide*.
