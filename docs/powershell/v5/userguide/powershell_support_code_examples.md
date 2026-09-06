---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/powershell_support_code_examples.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# Support examples using Tools for PowerShell V5
<a name="powershell_support_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with Support.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Add-ASACommunicationToCase`
<a name="support_AddCommunicationToCase_powershell_topic"></a>

The following code example shows how to use `Add-ASACommunicationToCase`.

**Tools for PowerShell V5**
**Example 1: Adds the body of an email communication to the specified case.**

```
Add-ASACommunicationToCase -CaseId "case-12345678910-2013-c4c1d2bf33c5cf47" -CommunicationBody "Some text about the case"
```
**Example 2: Adds the body of an email communication to the specified case plus one or more email addresses contained in the CC line of the email.**

```
Add-ASACommunicationToCase -CaseId "case-12345678910-2013-c4c1d2bf33c5cf47" -CcEmailAddress @("email1@address.com", "email2@address.com") -CommunicationBody "Some text about the case"
```
+  For API details, see [AddCommunicationToCase](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ASACase`
<a name="support_DescribeCases_powershell_topic"></a>

The following code example shows how to use `Get-ASACase`.

**Tools for PowerShell V5**
**Example 1: Returns the details of all support cases.**

```
Get-ASACase
```
**Example 2: Returns the details of all support cases since the specified date and time.**

```
Get-ASACase -AfterTime "2013-09-10T03:06Z"
```
**Example 3: Returns the details of the first 10 support cases, including those that have been resolved.**

```
Get-ASACase -MaxResult 10 -IncludeResolvedCases $true
```
**Example 4: Returns the details of the single specified support case.**

```
Get-ASACase -CaseIdList "case-12345678910-2013-c4c1d2bf33c5cf47"
```
**Example 5: Returns the details of specified support cases.**

```
Get-ASACase -CaseIdList @("case-12345678910-2013-c4c1d2bf33c5cf47", "case-18929034710-2011-c4fdeabf33c5cf47")
```
+  For API details, see [DescribeCases](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ASACommunication`
<a name="support_DescribeCommunications_powershell_topic"></a>

The following code example shows how to use `Get-ASACommunication`.

**Tools for PowerShell V5**
**Example 1: Returns all communications for the specified case.**

```
Get-ASACommunication -CaseId "case-12345678910-2013-c4c1d2bf33c5cf47"
```
**Example 2: Returns all communications since midnight UTC on January 1st 2012 for the specified case.**

```
Get-ASACommunication -CaseId "case-12345678910-2013-c4c1d2bf33c5cf47" -AfterTime "2012-01-10T00:00Z"
```
+  For API details, see [DescribeCommunications](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ASAService`
<a name="support_DescribeServices_powershell_topic"></a>

The following code example shows how to use `Get-ASAService`.

**Tools for PowerShell V5**
**Example 1: Returns all available service codes, names and categories.**

```
Get-ASAService
```
**Example 2: Returns the name and categories for the service with the specified code.**

```
Get-ASAService -ServiceCodeList "amazon-cloudfront"
```
**Example 3: Returns the name and categories for the specified service codes.**

```
Get-ASAService -ServiceCodeList @("amazon-cloudfront", "amazon-cloudwatch")
```
**Example 4: Returns the name and categories (in Japanese) for the specified service codes. Currently English ("en") and Japanese ("ja") language codes are supported.**

```
Get-ASAService -ServiceCodeList @("amazon-cloudfront", "amazon-cloudwatch") -Language "ja"
```
+  For API details, see [DescribeServices](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ASASeverityLevel`
<a name="support_DescribeSeverityLevels_powershell_topic"></a>

The following code example shows how to use `Get-ASASeverityLevel`.

**Tools for PowerShell V5**
**Example 1: Returns the list of severity levels that can be assigned to an AWS Support case.**

```
Get-ASASeverityLevel
```
**Example 2: Returns the list of severity levels that can be assigned to an AWS Support case. The names of the levels are returned in Japanese.**

```
Get-ASASeverityLevel -Language "ja"
```
+  For API details, see [DescribeSeverityLevels](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ASATrustedAdvisorCheck`
<a name="support_DescribeTrustedAdvisorChecks_powershell_topic"></a>

The following code example shows how to use `Get-ASATrustedAdvisorCheck`.

**Tools for PowerShell V5**
**Example 1: Returns the collection of Trusted Advisor checks. You must specify the Language parameter which can accept either "en" for English output or "ja" for Japanese output.**

```
Get-ASATrustedAdvisorCheck -Language "en"
```
+  For API details, see [DescribeTrustedAdvisorChecks](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ASATrustedAdvisorCheckRefreshStatus`
<a name="support_DescribeTrustedAdvisorCheckRefreshStatuses_powershell_topic"></a>

The following code example shows how to use `Get-ASATrustedAdvisorCheckRefreshStatus`.

**Tools for PowerShell V5**
**Example 1: Returns the current status of refresh requests for the specified checks. Request-ASATrustedAdvisorCheckRefresh can be used to request that the status information of the checks be refreshed.**

```
Get-ASATrustedAdvisorCheckRefreshStatus -CheckId @("checkid1", "checkid2")
```
+  For API details, see [DescribeTrustedAdvisorCheckRefreshStatuses](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ASATrustedAdvisorCheckResult`
<a name="support_DescribeTrustedAdvisorCheckResult_powershell_topic"></a>

The following code example shows how to use `Get-ASATrustedAdvisorCheckResult`.

**Tools for PowerShell V5**
**Example 1: Returns the results of a Trusted Advisor check. The list of available Trusted Advisor checks can be obtained using Get-ASATrustedAdvisorChecks. The output is the overall status of the check, the timestamp at which the check was last run and the unique checkid for the specific check. To have the results output in Japanese, add the -Language "ja" parameter.**

```
Get-ASATrustedAdvisorCheckResult -CheckId "checkid1"
```
+  For API details, see [DescribeTrustedAdvisorCheckResult](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ASATrustedAdvisorCheckSummary`
<a name="support_DescribeTrustedAdvisorCheckSummaries_powershell_topic"></a>

The following code example shows how to use `Get-ASATrustedAdvisorCheckSummary`.

**Tools for PowerShell V5**
**Example 1: Returns the latest summary for the specified Trusted Advisor check.**

```
Get-ASATrustedAdvisorCheckSummary -CheckId "checkid1"
```
**Example 2: Returns the latest summaries for the specified Trusted Advisor checks.**

```
Get-ASATrustedAdvisorCheckSummary -CheckId @("checkid1", "checkid2")
```
+  For API details, see [DescribeTrustedAdvisorCheckSummaries](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-ASACase`
<a name="support_CreateCase_powershell_topic"></a>

The following code example shows how to use `New-ASACase`.

**Tools for PowerShell V5**
**Example 1: Creates a new case in the AWS Support Center. Values for the -ServiceCode and -CategoryCode parameters can be obtained using the Get-ASAService cmdlet. The value for the -SeverityCode parameter can be obtained using the Get-ASASeverityLevel cmdlet. The -IssueType parameter value can be either "customer-service" or "technical". If successful the AWS Support case number is output. By default the case will be handled in English, to use Japanese add the -Language "ja" parameter. The -ServiceCode, -CategoryCode, -Subject and -CommunicationBody parameters are mandatory. **

```
New-ASACase -ServiceCode "amazon-cloudfront" -CategoryCode "APIs" -SeverityCode "low" -Subject "subject text" -CommunicationBody "description of the case" -CcEmailAddress @("email1@domain.com", "email2@domain.com") -IssueType "technical"
```
+  For API details, see [CreateCase](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Request-ASATrustedAdvisorCheckRefresh`
<a name="support_RefreshTrustedAdvisorCheck_powershell_topic"></a>

The following code example shows how to use `Request-ASATrustedAdvisorCheckRefresh`.

**Tools for PowerShell V5**
**Example 1: Requests a refresh for the specified Trusted Advisor check.**

```
Request-ASATrustedAdvisorCheckRefresh -CheckId "checkid1"
```
+  For API details, see [RefreshTrustedAdvisorCheck](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Resolve-ASACase`
<a name="support_ResolveCase_powershell_topic"></a>

The following code example shows how to use `Resolve-ASACase`.

**Tools for PowerShell V5**
**Example 1: Returns the initial state of the specified case and the current state after the call to resolve it is completed.**

```
Resolve-ASACase -CaseId "case-12345678910-2013-c4c1d2bf33c5cf47"
```
+  For API details, see [ResolveCase](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.
