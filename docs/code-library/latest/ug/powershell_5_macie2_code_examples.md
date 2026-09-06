---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/powershell_5_macie2_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Macie examples using Tools for PowerShell V5
<a name="powershell_5_macie2_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with Macie.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Get-MAC2FindingList`
<a name="macie2_ListFindings_powershell_5_topic"></a>

The following code example shows how to use `Get-MAC2FindingList`.

**Tools for PowerShell V5**
**Example 1: Returns list of FindingIds for Findings containing a sensitive data detection with type "CREDIT\_CARD\_NUMBER" or "US\_SOCIAL\_SECURITY\_NUMBER"**

```
$criterionAddProperties = New-Object Amazon.Macie2.Model.CriterionAdditionalProperties

$criterionAddProperties.Eq = @(
"CREDIT_CARD_NUMBER"
"US_SOCIAL_SECURITY_NUMBER"
)

$FindingCriterion = @{
'classificationDetails.result.sensitiveData.detections.type' = [Amazon.Macie2.Model.CriterionAdditionalProperties]$criterionAddProperties
}

Get-MAC2FindingList -FindingCriteria_Criterion $FindingCriterion -MaxResult 5
```
+  For API details, see [ListFindings](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.
