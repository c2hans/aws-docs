---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/optional-additional-configuration-cloud9-environment-setup.html
---

# (Optional) Additional configuration: Cloud9 environment setup
<a name="optional-additional-configuration-cloud9-environment-setup"></a>

1. Ensure Python version is 3.8 and above.

1. Set up Python version 3.8 if it is not available (link:https://docs.aws.amazon.com/cloud9/latest/user-guide/sample-python.html).

   ```
   sudo amazon-linux-extras enable python3.8
   sudo yum install python3.8
   sudo update-alternatives --install /usr/bin/python python
   alias python='python3.8'
   sudo python -m pip install pip-tools
   python -m pip install pip-tools
   ```

1. (Optional) Update `/source/lambda/requirements.txt` as cloud9 does not support specific versions.

   ```
   arnparse
   aws-xray-sdk
   boto3
   botocore
   certifi
   charset-normalizer
   codeguru-profiler-agent
   future
   idna
   jmespath
   jsonpickle
   python-dateutil
   python2-secrets
   requests
   s3transfer
   six
   urllib3
   wrapt
   ```

## Guidance customizations
<a name="solution-customizations"></a>

### Forensic investigation instance
<a name="forensic-investigation-instance"></a>

We recommend using `M5.2Xlarge` instance to perform memory and disk investigation, and initial mount disk volume size as 512 GB to support up to 512 GB of memory. Based on the forensic tools, you can modify the instance type post deployment.

You can update this configuration based on the memory of the compromised instance.

1.  [Download the CLI tool to manage a SIFT install](https://github.com/teamdfir/sift-cli/releases/download/v1.13.1/sift-cli-linux).

   ```
   wget link:https://github.com/teamdfir/sift-cli/releases/download/v1.13.1/sift-cli-linux
   wget link:https://github.com/teamdfir/sift-cli/releases/download/v1.13.1/sift-cli-linux.sig
   wget link:https://github.com/teamdfir/sift-cli/releases/download/v1.13.1/sift-cli.pub
   ```

1. Replace the Image Builder document in `san-sift.yml` with S3 copy commands.

   Sample S3 command:

   ```
   aws s3 cp s3://mybucket/san-sift
   ```

**Note**
The Guidance uses SANS SIFT to build necessary tools required to perform forensic investigation, and the Amazon EC2 Image Builder to build SANS SIFT image.

### AWS Systems Manager documents
<a name="aws-systems-manager-documents"></a>

The Guidance uses SSM documents to perform memory acquisition, memory investigation, and disk investigation. You can update the tools leveraged in memory acquisition, memory investigation, and disk investigation with other tools based on forensic requirements.

### Memory acquisition
<a name="memory-acquisition"></a>

For memory acquisition, the Guidance provides a [sample SSM document](https://github.com/504ensicsLabs/LiME), which leverages Linux Memory Extractor (LiME) to perform memory acquisition.

You can update the memory acquisition step with other tools by updating the SSM commands. The sample command clones the GitHub link to set up LiME in the compromised instance. The updated SSM command below downloads the LiME components from an internal S3 bucket to the AWS account.

In SSM document `linux_lime-memory-acquisition.json`, change the following sample command from:

```
git clone link:https://github.com/504ensicsLabs/LiME
```

to:

```
aws s3 cp s3://mybucket/Lime
```

### Memory investigation
<a name="memory-investigation"></a>

You can update the memory investigation step with other tools by updating the SSM commands. The sample command clones the GitHub link to set up Volatility in the compromised instance. The updated command below downloads the Volatility components from an internal S3 bucket to the AWS account. The Guidance depends on the Volatility symbol table of the OS and kernel version of the compromised instance. The Volatility symbol table is a prerequisite to perform memory investigation.

For memory investigation, the Guidance provides a sample SSM document which leverages Volatility 3 to perform memory investigation.

In SSM document `lime-memory-load-investigation.json`, change the following command from:

```
git clone link:https://github.com/volatilityfoundation/volatility.git
```

to the sample command:

```
aws s3 cp s3://mybucket/volatility
```

### Disk investigation
<a name="disk-investigation"></a>

For disk investigation, the Guidance provides the sample command leveraging `log2timeline` to perform disk investigation.

You can update the memory investigation step with other tools by updating the SSM commands. The current sample leverages the SANS SIFT image which contains [Plaso](https://plaso.readthedocs.io/en/latest/) in the forensic instance.

**Note**
The forensic tools code shared in the section are example codes. You are responsible for managing and maintaining the tools used in the Guidance.

## Customization of CDK context configurations
<a name="customization-of-cdk-context-configurations"></a>

| CDK config | Default value | Description |
| --- | --- | --- |
|  **diskSize**  |  `512`  | Determines the disk size of forensic investigation instance. We recommend allocating the disk size more than RAM for the compromised instance. |
|  **vol3-symboltables-bucket**  |  `n/a` - leverages the bucket created | Bucket to store Volatility symbol tables based on kernel version of the compromised instance to perform memory forensics. Ensure forensic investigation IAM role is updated to and has read-only access to S3 bucket. |
|  **vol3-symboltables-key**  |  `/volatility3/symboltables/`  | Prefix in the vol3-symboltables-bucket to store the symbol tables. |
|  **customerManagedCMKArns:{ forensicsnsEncryptionKey: ""}**  | n/a | KMS key to encrypt the messages sent to SNS topic. |
|  **customerManagedCMKArns:{ forensicBucketEncryptionKey: ""}**  | n/a | KMS key to encrypt the objects stored in Amazon S3. |
|  **customerManagedCMKArns:{ ebsVolumeKey: ""}**  | n/a | KMS key to encrypt to EBS Volume. |
|  **ssmExecutionTimeout**  |  `1800`  | SSM timeout to perform forensic operation. It is set to `1800` seconds by default. |
|  **forensicBucketComplianceMode**  |  `false`  | True sets S3 object lock retention mode to compliance else to governance. Refer to [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html) for more details. |
|  **forensicBucketRetentionDays**  |  `30`  | Configures the retention period that protects an object version for a fixed amount of time. |
|  **applicationAccounts**  | \* | Contains the list of all accounts the forensic functions can assume role, and perform memory and disk acquisition. |
|  **ssm-documents-dir**  |  `0/ssm-documents`  | SSM directory in source code to load SSM documents into forensic account as part of the deployment. |
|  **ForensicImageName**  |  `sansift`  | Forensic AMI name stored in SSM Parameter Store. SSM Parameter Store will contain AMI ID of forensic investigation instance prebuilt with forensic tools. |
|  **ForensicIsolationInstanceProfileName**  |  `target_profile_name`  | Customer profile for isolation. By default it would be the profile provided by this Guidance’s CDK stack. |
|  **vpcInfo**  | [source,json] ---- "vpcInfo": { "vpcCidr": "10.1.0.0/16", "maxAZs": 2, "bastionInstance": false, "enableVpcFlowLog": true, "enableVPCEndpoints": true, "subnetConfig": [ { "cidrMask": 24, "name": "externalDMZ", "subnetType": "Public" }, { "cidrMask": 24, "name": "service", "subnetType": "Private" }, { "cidrMask": 24, "name": "database", "subnetType": "Isolated" }, { "cidrMask": 24, "name": "internalDMZ", "subnetType": "Isolated" } ] } ---- | Contains VPC configurations to create a new VPC. |
|  **vpcConfigDetails**  | [source,json] ---- "vpcConfigDetails": { "isExistingVPC": false, "enableVPCEndpoints": false, "enableVpcFlowLog": false } ---- | Contains details about existing VPC configurations<br />[source,json] ---- "isExistingVPC": false, "vpcID": "vpc-1234567890", ---- |
|  **deployApi**  |  `false`  | Setting it to `true` deploys GraphQL API.<br />Setting it to `false` will not deploy GraphQL API. |
|  **apiNotifications**  |  `false`  | Setting it to `true` turns on GraphQL API notification.<br />Setting it to `false` turns off GraphQL API notification. |
|  **apiAllowedIps**  | [] | Provides list of all IPs allowed to access AppSyncAPI. WAF is configured to restrict the IP address. |
|  **apiRateLimit**  |  `1000`  | WAF is configured with `ratelimit`. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Forensics Orchestrator for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
