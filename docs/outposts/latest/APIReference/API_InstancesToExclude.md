---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_InstancesToExclude.html
---

# InstancesToExclude
<a name="API_InstancesToExclude"></a>

User-specified instances that must not be stopped. These instances will not appear in the list of instances that AWS recommends to stop in order to free up capacity.

## Contents
<a name="API_InstancesToExclude_Contents"></a>

 ** AccountIds **   <a name="outposts-Type-InstancesToExclude-AccountIds"></a>
IDs of the accounts that own each instance that must not be stopped.
Type: Array of strings
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** Instances **   <a name="outposts-Type-InstancesToExclude-Instances"></a>
List of user-specified instances that must not be stopped.
Type: Array of strings
Length Constraints: Minimum length of 11. Maximum length of 32.
Pattern: `^i-[0-9a-z]+$`
Required: No

 ** Services **   <a name="outposts-Type-InstancesToExclude-Services"></a>
Names of the services that own each instance that must not be stopped in order to free up the capacity needed to run the capacity task.
Type: Array of strings
Valid Values: `AWS | EC2 | EKS | ELASTICACHE | ELB | RDS | ROUTE53`
Required: No

## See Also
<a name="API_InstancesToExclude_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/InstancesToExclude)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/InstancesToExclude)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/InstancesToExclude)
