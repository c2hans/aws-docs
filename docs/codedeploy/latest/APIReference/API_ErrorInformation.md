---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ErrorInformation.html
---

# ErrorInformation
<a name="API_ErrorInformation"></a>

Information about a deployment error.

## Contents
<a name="API_ErrorInformation_Contents"></a>

 ** code **   <a name="CodeDeploy-Type-ErrorInformation-code"></a>
For more information, see [Error Codes for AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/error-codes.html) in the [AWS CodeDeploy User Guide](https://docs.aws.amazon.com/codedeploy/latest/userguide).
The error code:
+ APPLICATION\_MISSING: The application was missing. This error code is most likely raised if the application is deleted after the deployment is created, but before it is started.
+ DEPLOYMENT\_GROUP\_MISSING: The deployment group was missing. This error code is most likely raised if the deployment group is deleted after the deployment is created, but before it is started.
+ HEALTH\_CONSTRAINTS: The deployment failed on too many instances to be successfully deployed within the instance health constraints specified.
+ HEALTH\_CONSTRAINTS\_INVALID: The revision cannot be successfully deployed within the instance health constraints specified.
+ IAM\_ROLE\_MISSING: The service role cannot be accessed.
+ IAM\_ROLE\_PERMISSIONS: The service role does not have the correct permissions.
+ INTERNAL\_ERROR: There was an internal error.
+ NO\_EC2\_SUBSCRIPTION: The calling account is not subscribed to Amazon EC2.
+ NO\_INSTANCES: No instances were specified, or no instances can be found.
+ OVER\_MAX\_INSTANCES: The maximum number of instances was exceeded.
+ THROTTLED: The operation was throttled because the calling account exceeded the throttling limits of one or more AWS services.
+ TIMEOUT: The deployment has timed out.
+ REVISION\_MISSING: The revision ID was missing. This error code is most likely raised if the revision is deleted after the deployment is created, but before it is started.
Type: String
Valid Values: `AGENT_ISSUE | ALARM_ACTIVE | APPLICATION_MISSING | AUTOSCALING_VALIDATION_ERROR | AUTO_SCALING_CONFIGURATION | AUTO_SCALING_IAM_ROLE_PERMISSIONS | CODEDEPLOY_RESOURCE_CANNOT_BE_FOUND | CUSTOMER_APPLICATION_UNHEALTHY | DEPLOYMENT_GROUP_MISSING | ECS_UPDATE_ERROR | ELASTIC_LOAD_BALANCING_INVALID | ELB_INVALID_INSTANCE | HEALTH_CONSTRAINTS | HEALTH_CONSTRAINTS_INVALID | HOOK_EXECUTION_FAILURE | IAM_ROLE_MISSING | IAM_ROLE_PERMISSIONS | INTERNAL_ERROR | INVALID_ECS_SERVICE | INVALID_LAMBDA_CONFIGURATION | INVALID_LAMBDA_FUNCTION | INVALID_REVISION | MANUAL_STOP | MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION | MISSING_ELB_INFORMATION | MISSING_GITHUB_TOKEN | NO_EC2_SUBSCRIPTION | NO_INSTANCES | OVER_MAX_INSTANCES | RESOURCE_LIMIT_EXCEEDED | REVISION_MISSING | THROTTLED | TIMEOUT | CLOUDFORMATION_STACK_FAILURE | INVALID_EKS_CLUSTER | KUBERNETES_UPDATE_ERROR`
Required: No

 ** message **   <a name="CodeDeploy-Type-ErrorInformation-message"></a>
An accompanying error message.
Type: String
Required: No

## See Also
<a name="API_ErrorInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/ErrorInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/ErrorInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/ErrorInformation)
