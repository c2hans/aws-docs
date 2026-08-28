---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_KxScalingGroupConfiguration.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# KxScalingGroupConfiguration
<a name="API_KxScalingGroupConfiguration"></a>

The structure that stores the capacity configuration details of a scaling group.

## Contents
<a name="API_KxScalingGroupConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** memoryReservation **   <a name="finspace-Type-KxScalingGroupConfiguration-memoryReservation"></a>
 A reservation of the minimum amount of memory that should be available on the scaling group for a kdb cluster to be successfully placed in a scaling group.
Type: Integer
Valid Range: Minimum value of 6.
Required: Yes

 ** nodeCount **   <a name="finspace-Type-KxScalingGroupConfiguration-nodeCount"></a>
 The number of kdb cluster nodes.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** scalingGroupName **   <a name="finspace-Type-KxScalingGroupConfiguration-scalingGroupName"></a>
A unique identifier for the kdb scaling group.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: Yes

 ** cpu **   <a name="finspace-Type-KxScalingGroupConfiguration-cpu"></a>
 The number of vCPUs that you want to reserve for each node of this kdb cluster on the scaling group host.
Type: Double
Valid Range: Minimum value of 0.1.
Required: No

 ** memoryLimit **   <a name="finspace-Type-KxScalingGroupConfiguration-memoryLimit"></a>
 An optional hard limit on the amount of memory a kdb cluster can use.
Type: Integer
Valid Range: Minimum value of 6.
Required: No

## See Also
<a name="API_KxScalingGroupConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/KxScalingGroupConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/KxScalingGroupConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/KxScalingGroupConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
