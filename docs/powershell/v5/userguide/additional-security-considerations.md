---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/additional-security-considerations.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# Additional security considerations for the Tools for PowerShell
<a name="additional-security-considerations"></a>

This topic contains security considerations in addition to the security topics covered in earlier sections.

## Logging of sensitive information
<a name="add-sec-cons-sensitive-logs"></a>

Some operations of this tool might return information that could be considered sensitive, including information from environment variables. The exposure of this information might represent a security risk in certain scenarios; for example, the information could be included in continuous integration and continuous deployment (CI/CD) logs. It is therefore important that you review when you are including such output as part of your logs, and suppress the output when not needed. For additional information about protecting sensitive data, see [Data protection in this AWS product or service](pstools-security-data-protection.md).

Version 5 (V5) of the AWS Tools for PowerShell has been updated to exclude potentially sensitive information from logs by default. If you need to revert to tool behavior that could result in sensitive information being logged, you can do so for a particular PowerShell session by running the following command:

```
Set-AWSSensitiveDataConfiguration -ShowSensitiveData $true
```

If you do revert to previous tool behavior, you are increasing the risk that sensitive information might be logged. In this case, you should consider the following best practices:
+ Do not use environment variables to store sensitive values for your serverless resources. Instead have your serverless code programmatically retrieve the secret from a secrets store (for example, AWS Secrets Manager).
+ Review the contents of your build logs to ensure they do not contain sensitive information. Consider approaches such as piping to /dev/null or capturing the output as a bash or PowerShell variable to suppress command outputs.
+ Consider the access of your logs and scope the access appropriately for your use case.
