---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/powershell_5_route-53_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Route 53 examples using Tools for PowerShell V5
<a name="powershell_5_route-53_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with Route 53.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Edit-R53ResourceRecordSet`
<a name="route-53_ChangeResourceRecordSets_powershell_5_topic"></a>

The following code example shows how to use `Edit-R53ResourceRecordSet`.

**Tools for PowerShell V5**
**Example 1: This example creates an A record for www.example.com and changes the A record for test.example.com from 192.0.2.3 to 192.0.2.1. Note that values for changes TXT-type records must be in double quotes. See the Amazon Route 53 documentation for more details. You can use the Get-R53Change cmdlet to poll to determine when the changes are complete.**

```
$change1 = New-Object Amazon.Route53.Model.Change
$change1.Action = "CREATE"
$change1.ResourceRecordSet = New-Object Amazon.Route53.Model.ResourceRecordSet
$change1.ResourceRecordSet.Name = "www.example.com"
$change1.ResourceRecordSet.Type = "TXT"
$change1.ResourceRecordSet.TTL = 600
$change1.ResourceRecordSet.ResourceRecords = @()
$change1.ResourceRecordSet.ResourceRecords.Add(@{Value="item 1 item 2 item 3"})

$change2 = New-Object Amazon.Route53.Model.Change
$change2.Action = "DELETE"
$change2.ResourceRecordSet = New-Object Amazon.Route53.Model.ResourceRecordSet
$change2.ResourceRecordSet.Name = "test.example.com"
$change2.ResourceRecordSet.Type = "A"
$change2.ResourceRecordSet.TTL = 600
$change2.ResourceRecordSet.ResourceRecords = @()
$change2.ResourceRecordSet.ResourceRecords.Add(@{Value="192.0.2.3"})

$change3 = New-Object Amazon.Route53.Model.Change
$change3.Action = "CREATE"
$change3.ResourceRecordSet = New-Object Amazon.Route53.Model.ResourceRecordSet
$change3.ResourceRecordSet.Name = "test.example.com"
$change3.ResourceRecordSet.Type = "A"
$change3.ResourceRecordSet.TTL = 600
$change3.ResourceRecordSet.ResourceRecords = @()
$change3.ResourceRecordSet.ResourceRecords.Add(@{Value="192.0.2.1"})

$params = @{
    HostedZoneId="Z1PA6795UKMFR9"
	ChangeBatch_Comment="This change batch creates a TXT record for www.example.com. and changes the A record for test.example.com. from 192.0.2.3 to 192.0.2.1."
	ChangeBatch_Change=$change1,$change2,$change3
}

Edit-R53ResourceRecordSet @params
```
**Example 2: This example shows how to create alias resource record sets. 'Z222222222' is the ID of the Amazon Route 53 hosted zone in which you're creating the alias resource record set. 'example.com' is the zone apex for which you want to create an alias and 'www.example.com' is a subdomain for which you also want to create an alias. 'Z1111111111111' is an example of a hosted zone ID for the load balancer and 'example-load-balancer-1111111111.us-east-1.elb.amazonaws.com' is an example of a load balancer domain name with which Amazon Route 53 responds to queries for example.com and www.example.com. See the Amazon Route 53 documentation for more details. You can use the Get-R53Change cmdlet to poll to determine when the changes are complete.**

```
$change1 = New-Object Amazon.Route53.Model.Change
$change1.Action = "CREATE"
$change1.ResourceRecordSet = New-Object Amazon.Route53.Model.ResourceRecordSet
$change1.ResourceRecordSet.Name = "example.com"
$change1.ResourceRecordSet.Type = "A"
$change1.ResourceRecordSet.AliasTarget = New-Object Amazon.Route53.Model.AliasTarget
$change1.ResourceRecordSet.AliasTarget.HostedZoneId = "Z1111111111111"
$change1.ResourceRecordSet.AliasTarget.DNSName = "example-load-balancer-1111111111.us-east-1.elb.amazonaws.com."
$change1.ResourceRecordSet.AliasTarget.EvaluateTargetHealth = $true

$change2 = New-Object Amazon.Route53.Model.Change
$change2.Action = "CREATE"
$change2.ResourceRecordSet = New-Object Amazon.Route53.Model.ResourceRecordSet
$change1.ResourceRecordSet.Name = "www.example.com"
$change1.ResourceRecordSet.Type = "A"
$change1.ResourceRecordSet.AliasTarget = New-Object Amazon.Route53.Model.AliasTarget
$change1.ResourceRecordSet.AliasTarget.HostedZoneId = "Z1111111111111"
$change1.ResourceRecordSet.AliasTarget.DNSName = "example-load-balancer-1111111111.us-east-1.elb.amazonaws.com."
$change1.ResourceRecordSet.AliasTarget.EvaluateTargetHealth = $false

$params = @{
    HostedZoneId="Z222222222"
	ChangeBatch_Comment="This change batch creates two alias resource record sets, one for the zone apex, example.com, and one for www.example.com, that both point to example-load-balancer-1111111111.us-east-1.elb.amazonaws.com."
	ChangeBatch_Change=$change1,$change2
}

Edit-R53ResourceRecordSet @params
```
**Example 3: This example creates two A records for www.example.com. One-fourth of the time (1/(1\+3)), Amazon Route 53 responds to queries for www.example.com with the two values for the first resource record set (192.0.2.9 and 192.0.2.10). Three-fourths of the time (3/(1\+3)) Amazon Route 53 responds to queries for www.example.com with the two values for the second resource record set (192.0.2.11 and 192.0.2.12). See the Amazon Route 53 documentation for more details. You can use the Get-R53Change cmdlet to poll to determine when the changes are complete.**

```
$change1 = New-Object Amazon.Route53.Model.Change
$change1.Action = "CREATE"
$change1.ResourceRecordSet = New-Object Amazon.Route53.Model.ResourceRecordSet
$change1.ResourceRecordSet.Name = "www.example.com"
$change1.ResourceRecordSet.Type = "A"
$change1.ResourceRecordSet.SetIdentifier = "Rack 2, Positions 4 and 5"
$change1.ResourceRecordSet.Weight = 1
$change1.ResourceRecordSet.TTL = 600
$change1.ResourceRecordSet.ResourceRecords = @()
$change1.ResourceRecordSet.ResourceRecords.Add(@{Value="192.0.2.9"})
$change1.ResourceRecordSet.ResourceRecords.Add(@{Value="192.0.2.10"})

$change2 = New-Object Amazon.Route53.Model.Change
$change2.Action = "CREATE"
$change2.ResourceRecordSet = New-Object Amazon.Route53.Model.ResourceRecordSet
$change2.ResourceRecordSet.Name = "www.example.com"
$change2.ResourceRecordSet.Type = "A"
$change2.ResourceRecordSet.SetIdentifier = "Rack 5, Positions 1 and 2"
$change2.ResourceRecordSet.Weight = 3
$change2.ResourceRecordSet.TTL = 600
$change2.ResourceRecordSet.ResourceRecords = @()
$change2.ResourceRecordSet.ResourceRecords.Add(@{Value="192.0.2.11"})
$change2.ResourceRecordSet.ResourceRecords.Add(@{Value="192.0.2.12"})

$params = @{
    HostedZoneId="Z1PA6795UKMFR9"
    ChangeBatch_Comment="This change creates two weighted resource record sets, each of which has two values."
    ChangeBatch_Change=$change1,$change2
}

Edit-R53ResourceRecordSet @params
```
**Example 4: This example shows how to create weighted alias resource record sets assuming that example.com is the domain for which you want to create weighted alias resource record sets. SetIdentifier differentiates the two weighted alias resource record sets from one another. This element is required because the Name and Type elements have the same values for both resource record sets. Z1111111111111 and Z3333333333333 are examples of hosted zone IDs for the ELB load balancer specified by the value of DNSName. example-load-balancer-2222222222.us-east-1.elb.amazonaws.com and example-load-balancer-4444444444.us-east-1.elb.amazonaws.com are examples of Elastic Load Balancing domains from which Amazon Route 53 responds to queries for example.com. See the Amazon Route 53 documentation for more details. You can use the Get-R53Change cmdlet to poll to determine when the changes are complete.**

```
$change1 = New-Object Amazon.Route53.Model.Change
$change1.Action = "CREATE"
$change1.ResourceRecordSet = New-Object Amazon.Route53.Model.ResourceRecordSet
$change1.ResourceRecordSet.Name = "example.com"
$change1.ResourceRecordSet.Type = "A"
$change1.ResourceRecordSet.SetIdentifier = "1"
$change1.ResourceRecordSet.Weight = 3
$change1.ResourceRecordSet.AliasTarget = New-Object Amazon.Route53.Model.AliasTarget
$change1.ResourceRecordSet.AliasTarget.HostedZoneId = "Z1111111111111"
$change1.ResourceRecordSet.AliasTarget.DNSName = "example-load-balancer-2222222222.us-east-1.elb.amazonaws.com."
$change1.ResourceRecordSet.AliasTarget.EvaluateTargetHealth = $true

$change2 = New-Object Amazon.Route53.Model.Change
$change2.Action = "CREATE"
$change2.ResourceRecordSet = New-Object Amazon.Route53.Model.ResourceRecordSet
$change2.ResourceRecordSet.Name = "example.com"
$change2.ResourceRecordSet.Type = "A"
$change2.ResourceRecordSet.SetIdentifier = "2"
$change2.ResourceRecordSet.Weight = 1
$change2.ResourceRecordSet.AliasTarget = New-Object Amazon.Route53.Model.AliasTarget
$change2.ResourceRecordSet.AliasTarget.HostedZoneId = "Z3333333333333"
$change2.ResourceRecordSet.AliasTarget.DNSName = "example-load-balancer-4444444444.us-east-1.elb.amazonaws.com."
$change2.ResourceRecordSet.AliasTarget.EvaluateTargetHealth = $false

$params = @{
    HostedZoneId="Z5555555555"
    ChangeBatch_Comment="This change batch creates two weighted alias resource record sets. Amazon Route 53 responds to queries for example.com with the first ELB domain 3/4ths of the times and the second one 1/4th of the time."
    ChangeBatch_Change=$change1,$change2
}

Edit-R53ResourceRecordSet @params
```
**Example 5: This example creates two latency alias resource record sets, one for an ELB load balancer in the US West (Oregon) region (us-west-2), and another for a load balancer in the Asia Pacific (Singapore) region (ap-southeast-1). See the Amazon Route 53 documentation for more details. You can use the Get-R53Change cmdlet to poll to determine when the changes are complete.**

```
$change1 = New-Object Amazon.Route53.Model.Change
$change1.Action = "CREATE"
$change1.ResourceRecordSet = New-Object Amazon.Route53.Model.ResourceRecordSet
$change1.ResourceRecordSet.Name = "example.com"
$change1.ResourceRecordSet.Type = "A"
$change1.ResourceRecordSet.SetIdentifier = "Oregon load balancer 1"
$change1.ResourceRecordSet.Region = us-west-2
$change1.ResourceRecordSet.AliasTarget = New-Object Amazon.Route53.Model.AliasTarget
$change1.ResourceRecordSet.AliasTarget.HostedZoneId = "Z1111111111111"
$change1.ResourceRecordSet.AliasTarget.DNSName = "example-load-balancer-2222222222.us-west-2.elb.amazonaws.com"
$change1.ResourceRecordSet.AliasTarget.EvaluateTargetHealth = $true

$change2 = New-Object Amazon.Route53.Model.Change
$change2.Action = "CREATE"
$change2.ResourceRecordSet = New-Object Amazon.Route53.Model.ResourceRecordSet
$change2.ResourceRecordSet.Name = "example.com"
$change2.ResourceRecordSet.Type = "A"
$change2.ResourceRecordSet.SetIdentifier = "Singapore load balancer 1"
$change2.ResourceRecordSet.Region = ap-southeast-1
$change2.ResourceRecordSet.AliasTarget = New-Object Amazon.Route53.Model.AliasTarget
$change2.ResourceRecordSet.AliasTarget.HostedZoneId = "Z2222222222222"
$change2.ResourceRecordSet.AliasTarget.DNSName = "example-load-balancer-1111111111.ap-southeast-1.elb.amazonaws.com"
$change2.ResourceRecordSet.AliasTarget.EvaluateTargetHealth = $true

$params = @{
    HostedZoneId="Z5555555555"
    ChangeBatch_Comment="This change batch creates two latency resource record sets, one for the US West (Oregon) region and one for the Asia Pacific (Singapore) region."
    ChangeBatch_Change=$change1,$change2
}

Edit-R53ResourceRecordSet @params
```
+  For API details, see [ChangeResourceRecordSets](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-R53AccountLimit`
<a name="route-53_GetAccountLimit_powershell_5_topic"></a>

The following code example shows how to use `Get-R53AccountLimit`.

**Tools for PowerShell V5**
**Example 1: This example returns the maximum number of hosted zones that can be created using the current account.**

```
Get-R53AccountLimit -Type MAX_HOSTED_ZONES_BY_OWNER
```
**Output:**

```
15
```
+  For API details, see [GetAccountLimit](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-R53CheckerIpRanges`
<a name="route-53_GetCheckerIpRanges_powershell_5_topic"></a>

The following code example shows how to use `Get-R53CheckerIpRanges`.

**Tools for PowerShell V5**
**Example 1: This example returns the CIDRs for the Route53 health checkers**

```
Get-R53CheckerIpRanges
```
**Output:**

```
15.177.2.0/23
15.177.6.0/23
15.177.10.0/23
15.177.14.0/23
15.177.18.0/23
15.177.22.0/23
15.177.26.0/23
15.177.30.0/23
15.177.34.0/23
15.177.38.0/23
15.177.42.0/23
15.177.46.0/23
15.177.50.0/23
15.177.54.0/23
15.177.58.0/23
15.177.62.0/23
54.183.255.128/26
54.228.16.0/26
54.232.40.64/26
54.241.32.64/26
54.243.31.192/26
54.244.52.192/26
54.245.168.0/26
54.248.220.0/26
54.250.253.192/26
54.251.31.128/26
54.252.79.128/26
54.252.254.192/26
54.255.254.192/26
107.23.255.0/26
176.34.159.192/26
177.71.207.128/26
```
+  For API details, see [GetCheckerIpRanges](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-R53HostedZone`
<a name="route-53_GetHostedZone_powershell_5_topic"></a>

The following code example shows how to use `Get-R53HostedZone`.

**Tools for PowerShell V5**
**Example 1: Returns details of the hosted zone with ID Z1D633PJN98FT9.**

```
Get-R53HostedZone -Id Z1D633PJN98FT9
```
+  For API details, see [GetHostedZone](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-R53HostedZoneCount`
<a name="route-53_GetHostedZoneCount_powershell_5_topic"></a>

The following code example shows how to use `Get-R53HostedZoneCount`.

**Tools for PowerShell V5**
**Example 1: Returns the total number of public and private hosted zones for the current AWS account.**

```
Get-R53HostedZoneCount
```
+  For API details, see [GetHostedZoneCount](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-R53HostedZoneLimit`
<a name="route-53_GetHostedZoneLimit_powershell_5_topic"></a>

The following code example shows how to use `Get-R53HostedZoneLimit`.

**Tools for PowerShell V5**
**Example 1: This example returns the limit on the maximum number of records that can be created in the specified hosted zone.**

```
Get-R53HostedZoneLimit -HostedZoneId Z3MEQ8T7HAAAAF -Type MAX_RRSETS_BY_ZONE
```
**Output:**

```
5
```
+  For API details, see [GetHostedZoneLimit](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-R53HostedZoneList`
<a name="route-53_ListHostedZones_powershell_5_topic"></a>

The following code example shows how to use `Get-R53HostedZoneList`.

**Tools for PowerShell V5**
**Example 1: Outputs all of your public and private hosted zones.**

```
Get-R53HostedZoneList
```
**Example 2: Outputs all of the hosted zones that are associated with the reusable delegation set that has the ID NZ8X2CISAMPLE**

```
Get-R53HostedZoneList -DelegationSetId NZ8X2CISAMPLE
```
+  For API details, see [ListHostedZones](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-R53HostedZonesByName`
<a name="route-53_ListHostedZonesByName_powershell_5_topic"></a>

The following code example shows how to use `Get-R53HostedZonesByName`.

**Tools for PowerShell V5**
**Example 1: Returns all of your public and private hosted zones in ASCII order by domain name.**

```
Get-R53HostedZonesByName
```
**Example 2: Returns your public and private hosted zones, in ASCII order by domain name, starting at the specified DNS name.**

```
Get-R53HostedZonesByName -DnsName example2.com
```
+  For API details, see [ListHostedZonesByName](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-R53QueryLoggingConfigList`
<a name="route-53_ListQueryLoggingConfigs_powershell_5_topic"></a>

The following code example shows how to use `Get-R53QueryLoggingConfigList`.

**Tools for PowerShell V5**
**Example 1: This example returns all the configurations for DNS query logging that are associated with the current AWS account.**

```
Get-R53QueryLoggingConfigList
```
**Output:**

```
Id                                   HostedZoneId   CloudWatchLogsLogGroupArn
--                                   ------------   -------------------------
59b0fa33-4fea-4471-a88c-926476aaa40d Z385PDS6EAAAZR arn:aws:logs:us-east-1:111111111112:log-group:/aws/route53/example1.com:*
ee528e95-4e03-4fdc-9d28-9e24ddaaa063 Z94SJHBV1AAAAZ arn:aws:logs:us-east-1:111111111112:log-group:/aws/route53/example2.com:*
e38dddda-ceb6-45c1-8cb7-f0ae56aaaa2b Z3MEQ8T7AAA1BF arn:aws:logs:us-east-1:111111111112:log-group:/aws/route53/example3.com:*
```
+  For API details, see [ListQueryLoggingConfigs](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-R53ReusableDelegationSet`
<a name="route-53_GetReusableDelegationSet_powershell_5_topic"></a>

The following code example shows how to use `Get-R53ReusableDelegationSet`.

**Tools for PowerShell V5**
**Example 1: This example retrieves information about the specified delegation set including the four name servers that are assigned to the delegation set.**

```
Get-R53ReusableDelegationSet -Id N23DS9X4AYEAAA
```
**Output:**

```
Id                            CallerReference NameServers
--                            --------------- -----------
/delegationset/N23DS9X4AYEAAA testcaller      {ns-545.awsdns-04.net, ns-1264.awsdns-30.org, ns-2004.awsdns-58.co.uk, ns-240.awsdns-30.com}
```
+  For API details, see [GetReusableDelegationSet](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-R53HostedZone`
<a name="route-53_CreateHostedZone_powershell_5_topic"></a>

The following code example shows how to use `New-R53HostedZone`.

**Tools for PowerShell V5**
**Example 1: Creates a new hosted zone named 'example.com', associated with a reusable delegation set. Note that you must supply a value for the CallerReference parameter so that requests that need to be retried if necessary without the risk of executing the operation twice. Because the hosted zone is being created in a VPC it is automatically private and you should not set the -HostedZoneConfig\_PrivateZone parameter.**

```
$params = @{
    Name="example.com"
    CallerReference="myUniqueIdentifier"
    HostedZoneConfig_Comment="This is my first hosted zone"
    DelegationSetId="NZ8X2CISAMPLE"
    VPC_VPCId="vpc-1a2b3c4d"
    VPC_VPCRegion="us-east-1"
}

New-R53HostedZone @params
```
+  For API details, see [CreateHostedZone](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-R53QueryLoggingConfig`
<a name="route-53_CreateQueryLoggingConfig_powershell_5_topic"></a>

The following code example shows how to use `New-R53QueryLoggingConfig`.

**Tools for PowerShell V5**
**Example 1: This example creates a new Route53 DNS query logging configuration for the specified hosted zone. Amazon Route53 will publish DNS query logs to the specified Cloudwatch log group.**

```
New-R53QueryLoggingConfig -HostedZoneId Z3MEQ8T7HAAAAF -CloudWatchLogsLogGroupArn arn:aws:logs:us-east-1:111111111111:log-group:/aws/route53/example.com:*
```
**Output:**

```
QueryLoggingConfig                      Location
------------------                      --------
Amazon.Route53.Model.QueryLoggingConfig https://route53.amazonaws.com/2013-04-01/queryloggingconfig/ee5aaa95-4e03-4fdc-9d28-9e24ddaaaaa3
```
+  For API details, see [CreateQueryLoggingConfig](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-R53ReusableDelegationSet`
<a name="route-53_CreateReusableDelegationSet_powershell_5_topic"></a>

The following code example shows how to use `New-R53ReusableDelegationSet`.

**Tools for PowerShell V5**
**Example 1: This example creates a reusable delegation set of 4 name servers that can be resused by multiple hosted zones.**

```
New-R53ReusableDelegationSet -CallerReference testcallerreference
```
**Output:**

```
DelegationSet                      Location
-------------                      --------
Amazon.Route53.Model.DelegationSet https://route53.amazonaws.com/2013-04-01/delegationset/N23DS9XAAAAAXM
```
+  For API details, see [CreateReusableDelegationSet](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Register-R53VPCWithHostedZone`
<a name="route-53_AssociateVPCWithHostedZone_powershell_5_topic"></a>

The following code example shows how to use `Register-R53VPCWithHostedZone`.

**Tools for PowerShell V5**
**Example 1: This example associates the specified VPC with the private hosted zone.**

```
Register-R53VPCWithHostedZone -HostedZoneId Z3MEQ8T7HAAAAF -VPC_VPCId vpc-f1b9aaaa -VPC_VPCRegion us-east-1
```
**Output:**

```
Id                     Status  SubmittedAt         Comment
--                     ------  -----------         -------
/change/C3SCAAA633Z6DX PENDING 01/28/2020 19:32:02
```
+  For API details, see [AssociateVPCWithHostedZone](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-R53HostedZone`
<a name="route-53_DeleteHostedZone_powershell_5_topic"></a>

The following code example shows how to use `Remove-R53HostedZone`.

**Tools for PowerShell V5**
**Example 1: Deletes the hosted zone with the specified ID. You will be prompted for confirmation before the command proceeds unless you add the -Force switch parameter.**

```
Remove-R53HostedZone -Id Z1PA6795UKMFR9
```
+  For API details, see [DeleteHostedZone](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-R53QueryLoggingConfig`
<a name="route-53_DeleteQueryLoggingConfig_powershell_5_topic"></a>

The following code example shows how to use `Remove-R53QueryLoggingConfig`.

**Tools for PowerShell V5**
**Example 1: This example removes the specified configuration for DNS query logging.**

```
Remove-R53QueryLoggingConfig -Id ee528e95-4e03-4fdc-9d28-9e24daaa20063
```
+  For API details, see [DeleteQueryLoggingConfig](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-R53ReusableDelegationSet`
<a name="route-53_DeleteReusableDelegationSet_powershell_5_topic"></a>

The following code example shows how to use `Remove-R53ReusableDelegationSet`.

**Tools for PowerShell V5**
**Example 1: This example deletes the specified reusable delegation set.**

```
Remove-R53ReusableDelegationSet -Id N23DS9X4AYAAAM
```
+  For API details, see [DeleteReusableDelegationSet](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Unregister-R53VPCFromHostedZone`
<a name="route-53_DisassociateVPCFromHostedZone_powershell_5_topic"></a>

The following code example shows how to use `Unregister-R53VPCFromHostedZone`.

**Tools for PowerShell V5**
**Example 1: This example disassociates the specified VPC from the private hosted zone.**

```
Unregister-R53VPCFromHostedZone -HostedZoneId Z3MEQ8T7HAAAAF -VPC_VPCId vpc-f1b9aaaa -VPC_VPCRegion us-east-1
```
**Output:**

```
Id                     Status  SubmittedAt         Comment
--                     ------  -----------         -------
/change/C2XFCAAAA9HKZG PENDING 01/28/2020 10:35:55
```
+  For API details, see [DisassociateVPCFromHostedZone](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-R53HostedZoneComment`
<a name="route-53_UpdateHostedZoneComment_powershell_5_topic"></a>

The following code example shows how to use `Update-R53HostedZoneComment`.

**Tools for PowerShell V5**
**Example 1: This command updates the comment for the specified hosted zone.**

```
Update-R53HostedZoneComment -Id Z385PDS6AAAAAR -Comment "This is my first hosted zone"
```
**Output:**

```
Id                     : /hostedzone/Z385PDS6AAAAAR
Name                   : example.com.
CallerReference        : C5B55555-7147-EF04-8341-69131E805C89
Config                 : Amazon.Route53.Model.HostedZoneConfig
ResourceRecordSetCount : 9
LinkedService          :
```
+  For API details, see [UpdateHostedZoneComment](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
