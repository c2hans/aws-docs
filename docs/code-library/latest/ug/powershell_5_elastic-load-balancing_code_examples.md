---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/powershell_5_elastic-load-balancing_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Elastic Load Balancing - Version 1 examples using Tools for PowerShell V5
<a name="powershell_5_elastic-load-balancing_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with Elastic Load Balancing - Version 1.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Add-ELBLoadBalancerToSubnet`
<a name="elastic-load-balancing_AttachLoadBalancerToSubnets_powershell_5_topic"></a>

The following code example shows how to use `Add-ELBLoadBalancerToSubnet`.

**Tools for PowerShell V5**
**Example 1: This example adds the specified subnet to the set of subnets configured for the specified load balancer. The output includes the complete list of subnets.**

```
Add-ELBLoadBalancerToSubnet -LoadBalancerName my-load-balancer -Subnet subnet-12345678
```
**Output:**

```
subnet-12345678
subnet-87654321
```
+  For API details, see [AttachLoadBalancerToSubnets](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Add-ELBResourceTag`
<a name="elastic-load-balancing_AddTags_powershell_5_topic"></a>

The following code example shows how to use `Add-ELBResourceTag`.

**Tools for PowerShell V5**
**Example 1: This example adds the specified tags to the specified load balancer. The syntax used by this example requires PowerShell version 3 or later.**

```
Add-ELBResourceTag -LoadBalancerName my-load-balancer -Tag @{ Key="project";Value="lima" },@{ Key="department";Value="digital-media" }
```
**Example 2: With PowerShell version 2, you must use New-Object to create a tag for the Tag parameter.**

```
$tag = New-Object Amazon.ElasticLoadBalancing.Model.Tag
$tag.Key = "project"
$tag.Value = "lima"
Add-ELBResourceTag -LoadBalancerName my-load-balancer -Tag $tag
```
+  For API details, see [AddTags](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Disable-ELBAvailabilityZoneForLoadBalancer`
<a name="elastic-load-balancing_DisableAvailabilityZonesForLoadBalancer_powershell_5_topic"></a>

The following code example shows how to use `Disable-ELBAvailabilityZoneForLoadBalancer`.

**Tools for PowerShell V5**
**Example 1: This example removes the specified Availability Zone from the specified load balancer. The output includes the remaining Availability Zones.**

```
Disable-ELBAvailabilityZoneForLoadBalancer -LoadBalancerName my-load-balancer -AvailabilityZone us-west-2a
```
**Output:**

```
us-west-2b
```
+  For API details, see [DisableAvailabilityZonesForLoadBalancer](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Dismount-ELBLoadBalancerFromSubnet`
<a name="elastic-load-balancing_DetachLoadBalancerFromSubnets_powershell_5_topic"></a>

The following code example shows how to use `Dismount-ELBLoadBalancerFromSubnet`.

**Tools for PowerShell V5**
**Example 1: This example removes the specified subnet from the set of subnets configured for the specified load balancer. The output includes the remaining subnets.**

```
Dismount-ELBLoadBalancerFromSubnet -LoadBalancerName my-load-balancer -Subnet subnet-12345678
```
**Output:**

```
subnet-87654321
```
+  For API details, see [DetachLoadBalancerFromSubnets](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Edit-ELBLoadBalancerAttribute`
<a name="elastic-load-balancing_ModifyLoadBalancerAttributes_powershell_5_topic"></a>

The following code example shows how to use `Edit-ELBLoadBalancerAttribute`.

**Tools for PowerShell V5**
**Example 1: This example enables cross-zone load balancing for the specified load balancer.**

```
Edit-ELBLoadBalancerAttribute -LoadBalancerName my-load-balancer -CrossZoneLoadBalancing_Enabled $true
```
**Example 2: This example disables connection draining for the specified load balancer.**

```
Edit-ELBLoadBalancerAttribute -LoadBalancerName my-load-balancer -ConnectionDraining_Enabled $false
```
**Example 3: This example enables access logging for the specified load balancer.**

```
Edit-ELBLoadBalancerAttribute -LoadBalancerName my-load-balancer `
>> -AccessLog_Enabled $true `
>> -AccessLog_S3BucketName amzn-s3-demo-logging-bucket `
>> -AccessLog_S3BucketPrefix my-app/prod `
>> -AccessLog_EmitInterval 60
```
+  For API details, see [ModifyLoadBalancerAttributes](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Enable-ELBAvailabilityZoneForLoadBalancer`
<a name="elastic-load-balancing_EnableAvailabilityZonesForLoadBalancer_powershell_5_topic"></a>

The following code example shows how to use `Enable-ELBAvailabilityZoneForLoadBalancer`.

**Tools for PowerShell V5**
**Example 1: This example adds the specified Availability Zone to the specified load balancer. The output includes the complete list of Availability Zones.**

```
Enable-ELBAvailabilityZoneForLoadBalancer -LoadBalancerName my-load-balancer -AvailabilityZone us-west-2a
```
**Output:**

```
us-west-2a
us-west-2b
```
+  For API details, see [EnableAvailabilityZonesForLoadBalancer](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ELBInstanceHealth`
<a name="elastic-load-balancing_DescribeInstanceHealth_powershell_5_topic"></a>

The following code example shows how to use `Get-ELBInstanceHealth`.

**Tools for PowerShell V5**
**Example 1: This example describes the state of the instances registered with the specified load balancer.**

```
Get-ELBInstanceHealth -LoadBalancerName my-load-balancer
```
**Output:**

```
Description                   InstanceId                    ReasonCode                    State
-----------                   ----------                    ----------                    -----
N/A                           i-87654321                    N/A                           InService
Instance has failed at lea... i-12345678                    Instance                      OutOfService
```
**Example 2: This example describes the state of the specified instance registered with the specified load balancer.**

```
Get-ELBInstanceHealth -LoadBalancerName my-load-balancer -Instance i-12345678
```
**Example 3: This example displays the complete description of the state of the specified instance.**

```
(Get-ELBInstanceHealth -LoadBalancerName my-load-balancer -Instance i-12345678).Description
```
**Output:**

```
Instance has failed at least the UnhealthyThreshold number of health checks consecutively.
```
+  For API details, see [DescribeInstanceHealth](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ELBLoadBalancer`
<a name="elastic-load-balancing_DescribeLoadBalancers_powershell_5_topic"></a>

The following code example shows how to use `Get-ELBLoadBalancer`.

**Tools for PowerShell V5**
**Example 1: This example lists the names of your load balancers.**

```
Get-ELBLoadBalancer | format-table -property LoadBalancerName
```
**Output:**

```
LoadBalancerName
----------------
my-load-balancer
my-other-load-balancer
my-internal-load-balancer
```
**Example 2: This example describes the specified load balancer.**

```
Get-ELBLoadBalancer -LoadBalancerName my-load-balancer
```
**Output:**

```
AvailabilityZones         : {us-west-2a, us-west-2b}
BackendServerDescriptions : {Amazon.ElasticLoadBalancing.Model.BackendServerDescription}
CanonicalHostedZoneName   : my-load-balancer-1234567890.us-west-2.elb.amazonaws.com
CanonicalHostedZoneNameID : Z3DZXE0EXAMPLE
CreatedTime               : 4/11/2015 12:12:45 PM
DNSName                   : my-load-balancer-1234567890.us-west-2.elb.amazonaws.com
HealthCheck               : Amazon.ElasticLoadBalancing.Model.HealthCheck
Instances                 : {i-207d9717, i-afefb49b}
ListenerDescriptions      : {Amazon.ElasticLoadBalancing.Model.ListenerDescription}
LoadBalancerName          : my-load-balancer
Policies                  : Amazon.ElasticLoadBalancing.Model.Policies
Scheme                    : internet-facing
SecurityGroups            : {sg-a61988c3}
SourceSecurityGroup       : Amazon.ElasticLoadBalancing.Model.SourceSecurityGroup
Subnets                   : {subnet-15aaab61}
VPCId                     : vpc-a01106c2
```
**Example 3: This example describes all your load balancers in the current AWS region.**

```
Get-ELBLoadBalancer
```
**Example 4: This example describes all your load balancers across all available AWS Regions.**

```
Get-AWSRegion | % { Get-ELBLoadBalancer -Region $_ }
```
+  For API details, see [DescribeLoadBalancers](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ELBLoadBalancerAttribute`
<a name="elastic-load-balancing_DescribeLoadBalancerAttributes_powershell_5_topic"></a>

The following code example shows how to use `Get-ELBLoadBalancerAttribute`.

**Tools for PowerShell V5**
**Example 1: This example describes the attributes for the specified load balancer.**

```
Get-ELBLoadBalancerAttribute -LoadBalancerName my-load-balancer
```
**Output:**

```
AccessLog              : Amazon.ElasticLoadBalancing.Model.AccessLog
AdditionalAttributes   : {}
ConnectionDraining     : Amazon.ElasticLoadBalancing.Model.ConnectionDraining
ConnectionSettings     : Amazon.ElasticLoadBalancing.Model.ConnectionSettings
CrossZoneLoadBalancing : Amazon.ElasticLoadBalancing.Model.CrossZoneLoadBalancing
```
+  For API details, see [DescribeLoadBalancerAttributes](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ELBLoadBalancerPolicy`
<a name="elastic-load-balancing_DescribeLoadBalancerPolicies_powershell_5_topic"></a>

The following code example shows how to use `Get-ELBLoadBalancerPolicy`.

**Tools for PowerShell V5**
**Example 1: This example describes the policies associated with the specified load balancer.**

```
Get-ELBLoadBalancerPolicy -LoadBalancerName my-load-balancer
```
**Output:**

```
PolicyAttributeDescriptions             PolicyName                              PolicyTypeName
---------------------------             ----------                              --------------
{ProxyProtocol}                         my-ProxyProtocol-policy                 ProxyProtocolPolicyType
{CookieName}                            my-app-cookie-policy                    AppCookieStickinessPolicyType
```
**Example 2: This example describes the attributes of the specified policy.**

```
(Get-ELBLoadBalancerPolicy -LoadBalancerName my-load-balancer -PolicyName my-ProxyProtocol-policy).PolicyAttributeDescriptions
```
**Output:**

```
AttributeName    AttributeValue
-------------    --------------
ProxyProtocol    true
```
**Example 3: This example describes the predefined policies, including the sample policies. The names of the sample policies have the ELBSample- prefix.**

```
Get-ELBLoadBalancerPolicy
```
**Output:**

```
PolicyAttributeDescriptions             PolicyName                              PolicyTypeName
---------------------------             ----------                              --------------
{Protocol-SSLv2, Protocol-TLSv1, Pro... ELBSecurityPolicy-2015-05               SSLNegotiationPolicyType
{Protocol-SSLv2, Protocol-TLSv1, Pro... ELBSecurityPolicy-2015-03               SSLNegotiationPolicyType
{Protocol-SSLv2, Protocol-TLSv1, Pro... ELBSecurityPolicy-2015-02               SSLNegotiationPolicyType
{Protocol-SSLv2, Protocol-TLSv1, Pro... ELBSecurityPolicy-2014-10               SSLNegotiationPolicyType
{Protocol-SSLv2, Protocol-TLSv1, Pro... ELBSecurityPolicy-2014-01               SSLNegotiationPolicyType
{Protocol-SSLv2, Protocol-TLSv1, Pro... ELBSecurityPolicy-2011-08               SSLNegotiationPolicyType
{Protocol-SSLv2, Protocol-TLSv1, Pro... ELBSample-ELBDefaultCipherPolicy        SSLNegotiationPolicyType
{Protocol-SSLv2, Protocol-TLSv1, Pro... ELBSample-OpenSSLDefaultCipherPolicy    SSLNegotiationPolicyType
```
+  For API details, see [DescribeLoadBalancerPolicies](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ELBLoadBalancerPolicyType`
<a name="elastic-load-balancing_DescribeLoadBalancerPolicyTypes_powershell_5_topic"></a>

The following code example shows how to use `Get-ELBLoadBalancerPolicyType`.

**Tools for PowerShell V5**
**Example 1: This example gets the policy types supported by Elastic Load Balancing.**

```
Get-ELBLoadBalancerPolicyType
```
**Output:**

```
Description                             PolicyAttributeTypeDescriptions         PolicyTypeName
-----------                             -------------------------------         --------------
Stickiness policy with session lifet... {CookieExpirationPeriod}                LBCookieStickinessPolicyType
Policy that controls authentication ... {PublicKeyPolicyName}                   BackendServerAuthenticationPolicyType
Listener policy that defines the cip... {Protocol-SSLv2, Protocol-TLSv1, Pro... SSLNegotiationPolicyType
Policy containing a list of public k... {PublicKey}                             PublicKeyPolicyType
Stickiness policy with session lifet... {CookieName}                            AppCookieStickinessPolicyType
Policy that controls whether to incl... {ProxyProtocol}                         ProxyProtocolPolicyType
```
**Example 2: This example describes the specified policy type.**

```
Get-ELBLoadBalancerPolicyType -PolicyTypeName ProxyProtocolPolicyType
```
**Output:**

```
Description                             PolicyAttributeTypeDescriptions         PolicyTypeName
-----------                             -------------------------------         --------------
Policy that controls whether to incl... {ProxyProtocol}                         ProxyProtocolPolicyType
```
**Example 3: This example displays the complete description of the specified policy type.**

```
(Get-ELBLoadBalancerPolicyType -PolicyTypeName).Description
```
**Output:**

```
Policy that controls whether to include the IP address and port of the originating request for TCP messages.
This policy operates on TCP/SSL listeners only
```
+  For API details, see [DescribeLoadBalancerPolicyTypes](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ELBResourceTag`
<a name="elastic-load-balancing_DescribeTags_powershell_5_topic"></a>

The following code example shows how to use `Get-ELBResourceTag`.

**Tools for PowerShell V5**
**Example 1: This example lists the tags for the specified load balancers.**

```
Get-ELBResourceTag -LoadBalancerName @("my-load-balancer","my-internal-load-balancer")
```
**Output:**

```
LoadBalancerName             Tags
----------------             ----
my-load-balancer             {project, department}
my-internal-load-balancer    {project, department}
```
**Example 2: This example describes the tags for the specified load balancer.**

```
(Get-ELBResourceTag -LoadBalancerName my-load-balancer).Tags
```
**Output:**

```
Key           Value
---           -----
project       lima
department    digital-media
```
+  For API details, see [DescribeTags](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Join-ELBSecurityGroupToLoadBalancer`
<a name="elastic-load-balancing_ApplySecurityGroupsToLoadBalancer_powershell_5_topic"></a>

The following code example shows how to use `Join-ELBSecurityGroupToLoadBalancer`.

**Tools for PowerShell V5**
**Example 1: This example replaces the current security group for the specified load balancer with the specified security group.**

```
Join-ELBSecurityGroupToLoadBalancer -LoadBalancerName my-load-balancer -SecurityGroup sg-87654321
```
**Output:**

```
sg-87654321
```
**Example 2: To keep the current security group and specify an additional security group, specify both the existing and new security groups.**

```
Join-ELBSecurityGroupToLoadBalancer -LoadBalancerName my-load-balancer -SecurityGroup @("sg-12345678", "sg-87654321")
```
**Output:**

```
sg-12345678
sg-87654321
```
+  For API details, see [ApplySecurityGroupsToLoadBalancer](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-ELBAppCookieStickinessPolicy`
<a name="elastic-load-balancing_CreateAppCookieStickinessPolicy_powershell_5_topic"></a>

The following code example shows how to use `New-ELBAppCookieStickinessPolicy`.

**Tools for PowerShell V5**
**Example 1: This example creates a stickiness policy that follows the sticky session lifetimes of the specified application-generated cookie.**

```
New-ELBAppCookieStickinessPolicy -LoadBalancerName my-load-balancer -PolicyName my-app-cookie-policy -CookieName my-app-cookie
```
+  For API details, see [CreateAppCookieStickinessPolicy](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-ELBLBCookieStickinessPolicy`
<a name="elastic-load-balancing_CreateLbCookieStickinessPolicy_powershell_5_topic"></a>

The following code example shows how to use `New-ELBLBCookieStickinessPolicy`.

**Tools for PowerShell V5**
**Example 1: This example creates a stickiness policy with sticky session lifetimes controlled by the specified expiration period (in seconds).**

```
New-ELBLBCookieStickinessPolicy -LoadBalancerName my-load-balancer -PolicyName my-duration-cookie-policy -CookieExpirationPeriod 60
```
**Example 2: This example creates a stickiness policy with sticky session lifetimes controlled by the by the lifetime of the browser (user-agent).**

```
New-ELBLBCookieStickinessPolicy -LoadBalancerName my-load-balancer -PolicyName my-duration-cookie-policy
```
+  For API details, see [CreateLbCookieStickinessPolicy](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-ELBLoadBalancer`
<a name="elastic-load-balancing_CreateLoadBalancer_powershell_5_topic"></a>

The following code example shows how to use `New-ELBLoadBalancer`.

**Tools for PowerShell V5**
**Example 1: This example creates a load balancer with an HTTP listener in a VPC.**

```
$httpListener = New-Object Amazon.ElasticLoadBalancing.Model.Listener
$httpListener.Protocol = "http"
$httpListener.LoadBalancerPort = 80
$httpListener.InstanceProtocol = "http"
$httpListener.InstancePort = 80
New-ELBLoadBalancer -LoadBalancerName my-vpc-load-balancer -SecurityGroup sg-a61988c3 -Subnet subnet-15aaab61 -Listener $httpListener

my-vpc-load-balancer-1234567890.us-west-2.elb.amazonaws.com
```
**Example 2: This example creates a load balancer with an HTTP listener in EC2-Classic.**

```
New-ELBLoadBalancer -LoadBalancerName my-classic-load-balancer -AvailabilityZone us-west-2a` -Listener $httpListener
```
**Output:**

```
my-classic-load-balancer-123456789.us-west-2.elb.amazonaws.com
```
**Example 3: This example creates a load balancer with an HTTPS listener.**

```
$httpsListener = New-Object Amazon.ElasticLoadBalancing.Model.Listener
$httpsListener.Protocol = "https"
$httpsListener.LoadBalancerPort = 443
$httpsListener.InstanceProtocol = "http"
$httpsListener.InstancePort = 80
$httpsListener.SSLCertificateId="arn:aws:iam::123456789012:server-certificate/my-server-cert"
New-ELBLoadBalancer -LoadBalancerName my-load-balancer -AvailabilityZone us-west-2a -Listener $httpsListener

my-load-balancer-123456789.us-west-2.elb.amazonaws.com
```
+  For API details, see [CreateLoadBalancer](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-ELBLoadBalancerListener`
<a name="elastic-load-balancing_CreateLoadBalancerListeners_powershell_5_topic"></a>

The following code example shows how to use `New-ELBLoadBalancerListener`.

**Tools for PowerShell V5**
**Example 1: This example adds an HTTPS listener to the specified load balancer.**

```
$httpsListener = New-Object Amazon.ElasticLoadBalancing.Model.Listener
$httpsListener.Protocol = "https"
$httpsListener.LoadBalancerPort = 443
$httpsListener.InstanceProtocol = "https"
$httpsListener.InstancePort = 443
$httpsListener.SSLCertificateId="arn:aws:iam::123456789012:server-certificate/my-server-cert"
New-ELBLoadBalancerListener -LoadBalancerName my-load-balancer -Listener $httpsListener
```
+  For API details, see [CreateLoadBalancerListeners](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-ELBLoadBalancerPolicy`
<a name="elastic-load-balancing_CreateLoadBalancerPolicy_powershell_5_topic"></a>

The following code example shows how to use `New-ELBLoadBalancerPolicy`.

**Tools for PowerShell V5**
**Example 1: This example creates a new proxy protocol policy for a specified load balancer.**

```
$attribute = New-Object Amazon.ElasticLoadBalancing.Model.PolicyAttribute -Property @{
         AttributeName="ProxyProtocol"
         AttributeValue="True"
    }
New-ELBLoadBalancerPolicy -LoadBalancerName my-load-balancer -PolicyName my-ProxyProtocol-policy -PolicyTypeName ProxyProtocolPolicyType -PolicyAttribute $attribute
```
+  For API details, see [CreateLoadBalancerPolicy](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Register-ELBInstanceWithLoadBalancer`
<a name="elastic-load-balancing_RegisterInstancesWithLoadBalancer_powershell_5_topic"></a>

The following code example shows how to use `Register-ELBInstanceWithLoadBalancer`.

**Tools for PowerShell V5**
**Example 1: This example registers the specified EC2 instance with the specified load balancer.**

```
Register-ELBInstanceWithLoadBalancer -LoadBalancerName my-load-balancer -Instance i-12345678
```
**Output:**

```
InstanceId
----------
i-12345678
i-87654321
```
+  For API details, see [RegisterInstancesWithLoadBalancer](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-ELBInstanceFromLoadBalancer`
<a name="elastic-load-balancing_DeregisterInstancesFromLoadBalancer_powershell_5_topic"></a>

The following code example shows how to use `Remove-ELBInstanceFromLoadBalancer`.

**Tools for PowerShell V5**
**Example 1: This example removes the specified EC2 instance from the specified load balancer. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-ELBInstanceFromLoadBalancer -LoadBalancerName my-load-balancer -Instance i-12345678
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-ELBInstanceFromLoadBalancer (DeregisterInstancesFromLoadBalancer)" on Target
"Amazon.ElasticLoadBalancing.Model.Instance".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):

InstanceId
----------
i-87654321
```
+  For API details, see [DeregisterInstancesFromLoadBalancer](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-ELBLoadBalancer`
<a name="elastic-load-balancing_DeleteLoadBalancer_powershell_5_topic"></a>

The following code example shows how to use `Remove-ELBLoadBalancer`.

**Tools for PowerShell V5**
**Example 1: This example deletes the specified load balancer. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-ELBLoadBalancer -LoadBalancerName my-load-balancer
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-ELBLoadBalancer (DeleteLoadBalancer)" on Target "my-load-balancer".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteLoadBalancer](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-ELBLoadBalancerListener`
<a name="elastic-load-balancing_DeleteLoadBalancerListeners_powershell_5_topic"></a>

The following code example shows how to use `Remove-ELBLoadBalancerListener`.

**Tools for PowerShell V5**
**Example 1: This example deletes the listener on port 80 for the specified load balancer. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-ELBLoadBalancerListener -LoadBalancerName my-load-balancer -LoadBalancerPort 80
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-ELBLoadBalancerListener (DeleteLoadBalancerListeners)" on Target "80".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteLoadBalancerListeners](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-ELBLoadBalancerPolicy`
<a name="elastic-load-balancing_DeleteLoadBalancerPolicy_powershell_5_topic"></a>

The following code example shows how to use `Remove-ELBLoadBalancerPolicy`.

**Tools for PowerShell V5**
**Example 1: This example deletes the specified policy from the specified load balancer. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-ELBLoadBalancerPolicy -LoadBalancerName my-load-balancer -PolicyName my-duration-cookie-policy
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-ELBLoadBalancerPolicy (DeleteLoadBalancerPolicy)" on Target "my-duration-cookie-policy".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteLoadBalancerPolicy](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-ELBResourceTag`
<a name="elastic-load-balancing_RemoveTags_powershell_5_topic"></a>

The following code example shows how to use `Remove-ELBResourceTag`.

**Tools for PowerShell V5**
**Example 1: This example removes the specified tag from the specified load balancer. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter. The syntax used by this example requires PowerShell version 3 or later.**

```
Remove-ELBResourceTag -LoadBalancerName my-load-balancer -Tag @{ Key="project" }
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-ELBResourceTag (RemoveTags)" on target "Amazon.ElasticLoadBalancing.Model.TagKeyOnly".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
**Example 2: With Powershell version 2, you must use New-Object to create the tag for the Tag parameter.**

```
$tag = New-Object Amazon.ElasticLoadBalancing.Model.TagKeyOnly
$tag.Key = "project"
Remove-ELBResourceTag -Tag $tag -Force
```
+  For API details, see [RemoveTags](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Set-ELBHealthCheck`
<a name="elastic-load-balancing_ConfigureHealthCheck_powershell_5_topic"></a>

The following code example shows how to use `Set-ELBHealthCheck`.

**Tools for PowerShell V5**
**Example 1: This example configures the health check settings for the specified load balancer.**

```
Set-ELBHealthCheck -LoadBalancerName my-load-balancer `
>> -HealthCheck_HealthyThreshold 2 `
>> -HealthCheck_UnhealthyThreshold 2 `
>> -HealthCheck_Target "HTTP:80/ping" `
>> -HealthCheck_Interval 30 `
>> -HealthCheck_Timeout 3
```
**Output:**

```
HealthyThreshold   : 2
Interval           : 30
Target             : HTTP:80/ping
Timeout            : 3
UnhealthyThreshold : 2
```
+  For API details, see [ConfigureHealthCheck](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Set-ELBLoadBalancerListenerSSLCertificate`
<a name="elastic-load-balancing_SetLoadBalancerListenerSslCertificate_powershell_5_topic"></a>

The following code example shows how to use `Set-ELBLoadBalancerListenerSSLCertificate`.

**Tools for PowerShell V5**
**Example 1: This example replaces the certificate that terminates the SSL connections for the specified listener.**

```
Set-ELBLoadBalancerListenerSSLCertificate -LoadBalancerName my-load-balancer `
>> -LoadBalancerPort 443 `
>> -SSLCertificateId "arn:aws:iam::123456789012:server-certificate/new-server-cert"
```
+  For API details, see [SetLoadBalancerListenerSslCertificate](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Set-ELBLoadBalancerPolicyForBackendServer`
<a name="elastic-load-balancing_SetLoadBalancerPoliciesForBackendServer_powershell_5_topic"></a>

The following code example shows how to use `Set-ELBLoadBalancerPolicyForBackendServer`.

**Tools for PowerShell V5**
**Example 1: This example replaces the policies for the specified port with the specified policy.**

```
Set-ELBLoadBalancerPolicyForBackendServer -LoadBalancerName my-load-balancer -InstancePort 80 -PolicyName my-ProxyProtocol-policy
```
**Example 2: This example removes all policies associated with the specified port.**

```
Set-ELBLoadBalancerPolicyForBackendServer -LoadBalancerName my-load-balancer -InstancePort 80
```
+  For API details, see [SetLoadBalancerPoliciesForBackendServer](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Set-ELBLoadBalancerPolicyOfListener`
<a name="elastic-load-balancing_SetLoadBalancerPoliciesOfListener_powershell_5_topic"></a>

The following code example shows how to use `Set-ELBLoadBalancerPolicyOfListener`.

**Tools for PowerShell V5**
**Example 1: This example replaces the policies for the specified listener with the specified policy.**

```
Set-ELBLoadBalancerPolicyOfListener -LoadBalancerName my-load-balancer -LoadBalancerPort 443 -PolicyName my-SSLNegotiation-policy
```
**Example 2: This example removes all policies associated with the specified listener.**

```
Set-ELBLoadBalancerPolicyOfListener -LoadBalancerName my-load-balancer -LoadBalancerPort 443
```
+  For API details, see [SetLoadBalancerPoliciesOfListener](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.
