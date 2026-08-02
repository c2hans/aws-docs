---
source_url: https://docs.aws.amazon.com/powershell/v4/userguide/powershell_ses_code_examples.html
---

AWS Tools for PowerShell V4 has reached end of support.

We recommend that you migrate to [AWS Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/v5/userguide/). For additional details and information on how to migrate, please refer to our [end of support announcement](https://aws.amazon.com/blogs/developer/aws-tools-for-powershell-v4-end-of-support-announcement/).

# Amazon SES examples using Tools for PowerShell V4
<a name="powershell_ses_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V4 with Amazon SES.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Get-SESIdentity`
<a name="ses_ListIdentities_powershell_topic"></a>

The following code example shows how to use `Get-SESIdentity`.

**Tools for PowerShell V4**
**Example 1: This command returns a list containing all of the identities (email addresses and domains) for a specific AWS Account, regardless of verification status.**

```
Get-SESIdentity
```
+  For API details, see [ListIdentities](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SESSendQuota`
<a name="ses_GetSendQuota_powershell_topic"></a>

The following code example shows how to use `Get-SESSendQuota`.

**Tools for PowerShell V4**
**Example 1: This command returns the user's current sending limits.**

```
Get-SESSendQuota
```
+  For API details, see [GetSendQuota](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-SESSendStatistic`
<a name="ses_GetSendStatistics_powershell_topic"></a>

The following code example shows how to use `Get-SESSendStatistic`.

**Tools for PowerShell V4**
**Example 1: This command returns the user's sending statistics. The result is a list of data points, representing the last two weeks of sending activity. Each data point in the list contains statistics for a 15-minute interval.**

```
Get-SESSendStatistic
```
+  For API details, see [GetSendStatistics](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.
