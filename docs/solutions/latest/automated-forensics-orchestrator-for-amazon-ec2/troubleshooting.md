---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/troubleshooting.html
---

# Troubleshooting
<a name="troubleshooting"></a>

This section provides troubleshooting instructions for deploying and using the Guidance.

## Zero-byte files reported as part of memory and disk investigation
<a name="zero-byte-files"></a>

 **Issue** : The memory analysis and disk analysis results in S3 could result in zero-byte files.

 **Troubleshooting - zero-byte files**

![troubleshooting zero byte files](http://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/images/troubleshooting-zero-byte-files.png)

This could be a problem with the Volatility symbol table. Review the symbol table associated with the instance as well as the error logs in the Run Command history.

 **Troubleshooting - Run Command history**

![troubleshooting run command history](http://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/images/troubleshooting-run-command-history.png)

 **Resolution** : This is caused due to an error in SSM document run. Review the SSM error to fix the SSM document. It is necessary to review the Volatility symbol table and kernel version to ensure it matches the kernel version of running on the compromised EC2 instance.

## ForensicSecHubStack failed to deploy
<a name="forensicsechubstack-failed"></a>

 **Issue** : ForensicSecHubStack failed to deploy. Received response status [FAILED] from custom resource. Message returned: InvalidAccessException: An error occurred (InvalidAccessException) when calling the CreateActionTarget operation: Account {{<Account>}} is not subscribed to AWS Security Hub. See details in CloudWatch Log Stream.

 **Resolution** : Activate Security Hub and redeploy ForensicSecHubStack.
