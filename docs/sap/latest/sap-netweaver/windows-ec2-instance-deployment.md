---
source_url: https://docs.aws.amazon.com/sap/latest/sap-netweaver/windows-ec2-instance-deployment.html
---

# Windows EC2 Instance Deployment
<a name="windows-ec2-instance-deployment"></a>

Deciding the right storage layout is important to ensure you are able to meet required IO. Amazon EBS general purpose volume (gp2) provides 3 IOPS per GB whereas provisioned IOPS (io1) provide a max of 50 IOPS per GB. See [EBS features](https://aws.amazon.com/ebs/features/?nc=sn&loc=1) for details. If you decide to separate SQL data, log, and tempdb to different volumes, consider these aspects.

For gp2, with one volume for all (data, log, and tempdb). Create storage config file as below. Replace placeholder `<size>` as per your requirement.

```
[
    {
        "DeviceName": "xvdb",
        "Ebs": {
            "VolumeSize": <size>,
            "VolumeType": "gp2",
            "DeleteOnTermination": true
        }
    }
]
```

For separate volumes, gp2 (data), io1 (log) and io1 (tempdb) create storage configuration file as below. Replace placeholders `<size>` and `<IOPS Required>` with size of the disk and IOPS you need.

```
[
    {
        "DeviceName": "xvdb",
        "Ebs": {
            "VolumeSize": <size>,
            "VolumeType": "gp2",
            "DeleteOnTermination": true
        }
    },
    {
        "DeviceName": "xvdc",
        "Ebs": {
            "VolumeSize": <size>,
            "VolumeType": “io1",
            "Iops": <IOPS Required>,
            "DeleteOnTermination": true
        }
    },
    {
        "DeviceName": "xvdd",
        "Ebs": {
            "VolumeSize": <size>,
            "VolumeType": “io1",
            "Iops": <IOPS Required>,
            "DeleteOnTermination": true
        }
    }
]
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
