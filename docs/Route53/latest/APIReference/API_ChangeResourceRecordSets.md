---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeResourceRecordSets.html
---

# ChangeResourceRecordSets
<a name="API_ChangeResourceRecordSets"></a>

Creates, changes, or deletes a resource record set, which contains authoritative DNS information for a specified domain name or subdomain name. For example, you can use `ChangeResourceRecordSets` to create a resource record set that routes traffic for test.example.com to a web server that has an IP address of 192.0.2.44.

 **Deleting Resource Record Sets**

To delete a resource record set, you must specify all the same values that you specified when you created it.

 **Change Batches and Transactional Changes**

The request body must include a document with a `ChangeResourceRecordSetsRequest` element. The request body contains a list of change items, known as a change batch. Change batches are considered transactional changes. Route 53 validates the changes in the request and then either makes all or none of the changes in the change batch request. This ensures that DNS routing isn't adversely affected by partial changes to the resource record sets in a hosted zone.

For example, suppose a change batch request contains two changes: it deletes the `CNAME` resource record set for www.example.com and creates an alias resource record set for www.example.com. If validation for both records succeeds, Route 53 deletes the first resource record set and creates the second resource record set in a single operation. If validation for either the `DELETE` or the `CREATE` action fails, then the request is canceled, and the original `CNAME` record continues to exist.

**Note**
If you try to delete the same resource record set more than once in a single change batch, Route 53 returns an `InvalidChangeBatch` error.

 **Traffic Flow**

To create resource record sets for complex routing configurations, use either the traffic flow visual editor in the Route 53 console or the API actions for traffic policies and traffic policy instances. Save the configuration as a traffic policy, then associate the traffic policy with one or more domain names (such as example.com) or subdomain names (such as www.example.com), in the same hosted zone or in multiple hosted zones. You can roll back the updates if the new configuration isn't performing as expected. For more information, see [Using Traffic Flow to Route DNS Traffic](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/traffic-flow.html) in the *Amazon Route 53 Developer Guide*.

 **Create, Delete, and Upsert**

Use `ChangeResourceRecordsSetsRequest` to perform the following actions:
+  `CREATE`: Creates a resource record set that has the specified values.
+  `DELETE`: Deletes an existing resource record set that has the specified values.
+  `UPSERT`: If a resource set doesn't exist, Route 53 creates it. If a resource set exists Route 53 updates it with the values in the request.

 **Syntaxes for Creating, Updating, and Deleting Resource Record Sets**

The syntax for a request depends on the type of resource record set that you want to create, delete, or update, such as weighted, alias, or failover. The XML elements in your request must appear in the order listed in the syntax.

For syntax examples that show the elements for each kind of resource record set, such as basic, weighted, and alias, see the [Examples](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeResourceRecordSets.html#API_ChangeResourceRecordSets_Examples) section of `ChangeResourceRecordSets`.

Don't refer to the syntax in the "Syntax" section, which includes all of the elements for every kind of resource record set that you can create, delete, or update by using `ChangeResourceRecordSets`.

 **Change Propagation to Route 53 DNS Servers**

When you submit a `ChangeResourceRecordSets` request, Route 53 propagates your changes to all of the Route 53 authoritative DNS servers managing the hosted zone. While your changes are propagating, `GetChange` returns a status of `PENDING`. When propagation is complete, `GetChange` returns a status of `INSYNC`. Changes generally propagate to all Route 53 name servers managing the hosted zone within 60 seconds. For more information, see [GetChange](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html).

 **Limits on ChangeResourceRecordSets Requests**

For information about the limits on a `ChangeResourceRecordSets` request, see [Limits](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html) in the *Amazon Route 53 Developer Guide*.

## Request Syntax
<a name="API_ChangeResourceRecordSets_RequestSyntax"></a>

```
POST /2013-04-01/hostedzone/{{Id}}/rrset/ HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ChangeResourceRecordSetsRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <ChangeBatch>
      <Changes>
         <Change>
            <Action>{{string}}</Action>
            <ResourceRecordSet>
               <AliasTarget>
                  <DNSName>{{string}}</DNSName>
                  <EvaluateTargetHealth>{{boolean}}</EvaluateTargetHealth>
                  <HostedZoneId>{{string}}</HostedZoneId>
               </AliasTarget>
               <CidrRoutingConfig>
                  <CollectionId>{{string}}</CollectionId>
                  <LocationName>{{string}}</LocationName>
               </CidrRoutingConfig>
               <Failover>{{string}}</Failover>
               <GeoLocation>
                  <ContinentCode>{{string}}</ContinentCode>
                  <CountryCode>{{string}}</CountryCode>
                  <SubdivisionCode>{{string}}</SubdivisionCode>
               </GeoLocation>
               <GeoProximityLocation>
                  <AWSRegion>{{string}}</AWSRegion>
                  <Bias>{{integer}}</Bias>
                  <Coordinates>
                     <Latitude>{{string}}</Latitude>
                     <Longitude>{{string}}</Longitude>
                  </Coordinates>
                  <LocalZoneGroup>{{string}}</LocalZoneGroup>
               </GeoProximityLocation>
               <HealthCheckId>{{string}}</HealthCheckId>
               <MultiValueAnswer>{{boolean}}</MultiValueAnswer>
               <Name>{{string}}</Name>
               <Region>{{string}}</Region>
               <ResourceRecords>
                  <ResourceRecord>
                     <Value>{{string}}</Value>
                  </ResourceRecord>
               </ResourceRecords>
               <SetIdentifier>{{string}}</SetIdentifier>
               <TrafficPolicyInstanceId>{{string}}</TrafficPolicyInstanceId>
               <TTL>{{long}}</TTL>
               <Type>{{string}}</Type>
               <Weight>{{long}}</Weight>
            </ResourceRecordSet>
         </Change>
      </Changes>
      <Comment>{{string}}</Comment>
   </ChangeBatch>
</ChangeResourceRecordSetsRequest>
```

## URI Request Parameters
<a name="API_ChangeResourceRecordSets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_ChangeResourceRecordSets_RequestSyntax) **   <a name="Route53-ChangeResourceRecordSets-request-uri-HostedZoneId"></a>
The ID of the hosted zone that contains the resource record sets that you want to change.
Length Constraints: Maximum length of 32.
Required: Yes

## Request Body
<a name="API_ChangeResourceRecordSets_RequestBody"></a>

The request accepts the following data in XML format.

 ** [ChangeResourceRecordSetsRequest](#API_ChangeResourceRecordSets_RequestSyntax) **   <a name="Route53-ChangeResourceRecordSets-request-ChangeResourceRecordSetsRequest"></a>
Root level tag for the ChangeResourceRecordSetsRequest parameters.
Required: Yes

 ** [ChangeBatch](#API_ChangeResourceRecordSets_RequestSyntax) **   <a name="Route53-ChangeResourceRecordSets-request-ChangeBatch"></a>
A complex type that contains an optional comment and the `Changes` element.
Type: [ChangeBatch](API_ChangeBatch.md) object
Required: Yes

## Response Syntax
<a name="API_ChangeResourceRecordSets_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ChangeResourceRecordSetsResponse>
   <ChangeInfo>
      <Comment>string</Comment>
      <Id>string</Id>
      <Status>string</Status>
      <SubmittedAt>timestamp</SubmittedAt>
   </ChangeInfo>
</ChangeResourceRecordSetsResponse>
```

## Response Elements
<a name="API_ChangeResourceRecordSets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ChangeResourceRecordSetsResponse](#API_ChangeResourceRecordSets_ResponseSyntax) **   <a name="Route53-ChangeResourceRecordSets-response-ChangeResourceRecordSetsResponse"></a>
Root level tag for the ChangeResourceRecordSetsResponse parameters.
Required: Yes

 ** [ChangeInfo](#API_ChangeResourceRecordSets_ResponseSyntax) **   <a name="Route53-ChangeResourceRecordSets-response-ChangeInfo"></a>
A complex type that contains information about changes made to your hosted zone.
This element contains an ID that you use when performing a [GetChange](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html) action to get detailed information about the change.
Type: [ChangeInfo](API_ChangeInfo.md) object

## Errors
<a name="API_ChangeResourceRecordSets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidChangeBatch **
This exception contains a list of messages that might contain one or more error messages. Each error message indicates one error in the change batch.
 ** messages **

HTTP Status Code: 400

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchHealthCheck **
No health check exists with the specified ID.
 ** message **

HTTP Status Code: 404

 ** NoSuchHostedZone **
No hosted zone exists with the ID that you specified.
 ** message **

HTTP Status Code: 404

 ** PriorRequestNotComplete **
If Amazon Route 53 can't process a request before the next request arrives, it will reject subsequent requests for the same hosted zone and return an `HTTP 400 error` (`Bad request`). If Route 53 returns this error repeatedly for the same request, we recommend that you wait, in intervals of increasing duration, before you try the request again.
HTTP Status Code: 400

## Examples
<a name="API_ChangeResourceRecordSets_Examples"></a>

### Basic Syntax
<a name="API_ChangeResourceRecordSets_Example_1"></a>

This example illustrates one usage of ChangeResourceRecordSets.

```
POST /2013-04-01/hostedzone/Route 53 hosted zone ID/rrset HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ChangeResourceRecordSetsRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
<ChangeBatch>
   <Comment>optional comment about the changes in this change batch request</Comment>
   <Changes>
      <Change>
         <Action>CREATE | DELETE | UPSERT</Action>
         <ResourceRecordSet>
            <Name>fully qualified domain name</Name>
            <Type>DNS record type</Type>
            <TTL>time to live in seconds</TTL>
            <ResourceRecords>
               <ResourceRecord>
                  <Value>applicable value for the record type</Value>
               </ResourceRecord>
               ...
            </ResourceRecords>
            <HealthCheckId>optional ID of a Route 53 health check</HealthCheckId>
         </ResourceRecordSet>
      </Change>
      ...
   </Changes>
</ChangeBatch>
</ChangeResourceRecordSetsRequest>
```

### Alias Resource Record Set Syntax
<a name="API_ChangeResourceRecordSets_Example_2"></a>

For information about alias resource record sets, see [Choosing Between Alias and Non-Alias Resource Record Sets](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html) in the *Amazon Route 53 Developer Guide*.

```
POST /2013-04-01/hostedzone/Route 53 hosted zone ID/rrset HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ChangeResourceRecordSetsRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
<ChangeBatch>
   <Comment>optional comment about the changes in this change batch request</Comment>
   <Changes>
      <Change>
         <Action>CREATE | DELETE | UPSERT</Action>
         <ResourceRecordSet>
            <Name>fully qualified domain name</Name>
            <Type>DNS record type</Type>
            <AliasTarget>
               <HostedZoneId>hosted zone ID for your AWS resource or Route 53 hosted zone</HostedZoneId>
               <DNSName>DNS domain name for your AWS resource or another resource record set in this hosted zone</DNSName>
               <EvaluateTargetHealth>true | false</EvaluateTargetHealth>
            </AliasTarget>
            <HealthCheckId>optional ID of a Route 53 health check</HealthCheckId>
         </ResourceRecordSet>
      </Change>
      ...
   </Changes>
</ChangeBatch>
</ChangeResourceRecordSetsRequest>
```

### Failover Syntax
<a name="API_ChangeResourceRecordSets_Example_3"></a>

For information about configuring Route 53 failover, see the following topics in the *Amazon Route 53 Developer Guide*:
+  [Creating Route 53 Health Checks and Configuring DNS Failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html)
+  [Configuring Failover in a Private Hosted Zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html)

```
POST /2013-04-01/hostedzone/Route 53 hosted zone ID/rrset HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ChangeResourceRecordSetsRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
<ChangeBatch>
   <Comment>optional comment about the changes in this change batch request</Comment>
   <Changes>
      <Change>
         <Action>CREATE | DELETE | UPSERT</Action>
         <ResourceRecordSet>
            <Name>fully qualified domain name</Name>
            <Type>DNS record type</Type>
            <SetIdentifier>unique description for this resource record set</SetIdentifier>
            <Failover>PRIMARY | SECONDARY</Failover>
            <TTL>time to live in seconds</TTL>
            <ResourceRecords>
               <ResourceRecord>
                  <Value>applicable value for the record type</Value>
               </ResourceRecord>
               ...
            </ResourceRecords>
            <HealthCheckId>ID of a Route 53 health check</HealthCheckId>
         </ResourceRecordSet>
      </Change>
      ...
   </Changes>
</ChangeBatch>
</ChangeResourceRecordSetsRequest>
```

### Failover Alias Syntax
<a name="API_ChangeResourceRecordSets_Example_4"></a>

For more information, see the following topics in the *Amazon Route 53 Developer Guide*:
+  [Creating Route 53 Health Checks and Configuring DNS Failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html)
+  [Configuring Failover in a Private Hosted Zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html)
+  [Choosing Between Alias and Non-Alias Resource Record Sets](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html)

```
POST /2013-04-01/hostedzone/Route 53 hosted zone ID/rrset HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ChangeResourceRecordSetsRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
<ChangeBatch>
   <Comment>optional comment about the changes in this change batch request</Comment>
   <Changes>
      <Change>
         <Action>CREATE | DELETE | UPSERT</Action>
         <ResourceRecordSet>
            <Name>fully qualified domain name</Name>
            <Type>DNS record type</Type>
            <SetIdentifier>unique description for this resource record set</SetIdentifier>
            <Failover>PRIMARY | SECONDARY</Failover>
            <AliasTarget>
               <HostedZoneId>hosted zone ID for your AWS resource or Route 53 hosted zone</HostedZoneId>
               <DNSName>DNS domain name for your AWS resource or another resource record set in this hosted zone</DNSName>
               <EvaluateTargetHealth>true | false</EvaluateTargetHealth>
            </AliasTarget>
            <HealthCheckId>optional ID of a Route 53 health check</HealthCheckId>
         </ResourceRecordSet>
      </Change>
      ...
   </Changes>
</ChangeBatch>
</ChangeResourceRecordSetsRequest>
```

### Geolocation Syntax
<a name="API_ChangeResourceRecordSets_Example_5"></a>

For more information, see [Geolocation Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-geo) in the *Amazon Route 53 Developer Guide*.

```
POST /2013-04-01/hostedzone/Route 53 hosted zone ID/rrset HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ChangeResourceRecordSetsRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
<ChangeBatch>
   <Comment>optional comment about the changes in this
      change batch request</Comment>
   <Changes>
      <Change>
         <Action>CREATE | DELETE | UPSERT</Action>
         <ResourceRecordSet>
            <Name>fully qualified domain name</Name>
            <Type>DNS record type</Type>
            <SetIdentifier>unique description for this resource record set</SetIdentifier>
            <GeoLocation>
               <ContinentCode>two-letter continent code</ContinentCode>
               <CountryCode>two-letter country code</CountryCode>
               <SubdivisionCode>subdivision code</SubdivisionCode>
            </GeoLocation>
            <TTL>time to live in seconds</TTL>
            <ResourceRecords>
               <ResourceRecord>
                  <Value>applicable value for the record type</Value>
               </ResourceRecord>
               ...
            </ResourceRecords>
            <HealthCheckId>ID of a Route 53 health check</HealthCheckId>
         </ResourceRecordSet>
      </Change>
      ...
   </Changes>
</ChangeBatch>
</ChangeResourceRecordSetsRequest>
```

### Geolocation Alias Syntax
<a name="API_ChangeResourceRecordSets_Example_6"></a>

For more information, see the following topics in the *Amazon Route 53 Developer Guide*:
+  [Geolocation Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-geo)
+  [Choosing Between Alias and Non-Alias Resource Record Sets](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html)

```
POST /2013-04-01/hostedzone/Route 53 hosted zone ID/rrset HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ChangeResourceRecordSetsRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
<ChangeBatch>
   <Comment>optional comment about the changes in this
      change batch request</Comment>
   <Changes>
      <Change>
         <Action>CREATE | DELETE | UPSERT</Action>
         <ResourceRecordSet>
            <Name>fully qualified domain name</Name>
            <Type>DNS record type</Type>
            <SetIdentifier>unique description for this resource record set</SetIdentifier>
            <GeoLocation>
               <ContinentCode>two-letter continent code</ContinentCode>
               <CountryCode>two-letter country code</CountryCode>
               <SubdivisionCode>subdivision code</SubdivisionCode>
            </GeoLocation>
            <AliasTarget>
               <HostedZoneId>hosted zone ID for your AWS resource or Route 53 hosted zone</HostedZoneId>
               <DNSName>DNS domain name for your AWS resource or another resource record set in this hosted zone</DNSName>
               <EvaluateTargetHealth>true | false</EvaluateTargetHealth>
            </AliasTarget>
            <HealthCheckId>optional ID of a Route 53 health check</HealthCheckId>
         </ResourceRecordSet>
      </Change>
      ...
   </Changes>
</ChangeBatch>
</ChangeResourceRecordSetsRequest>
```

### Geoproximity Syntax when using coordinates
<a name="API_ChangeResourceRecordSets_Example_7"></a>

For more information, see [Geoproximity Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-geoproximity) in the *Amazon Route 53 Developer Guide*.

```
POST /2013-04-01/hostedzone/Route 53 hosted zone ID/rrset HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ChangeResourceRecordSetsRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
<ChangeBatch>
   <Comment>optional comment about the changes in this change batch request</Comment>
   <Changes>
      <Change>
         <Action>CREATE | DELETE | UPSERT</Action>
         <ResourceRecordSet>
           <Name>fully qualified domain name</Name>
            <Type>DNS record type</Type>
            <SetIdentifier>unique description for this resource record set</SetIdentifier>
            <TTL>time to live in seconds</TTL>
           <ResourceRecords>
               <ResourceRecord>
                  <Value>applicable value for the record type</Value>
               </ResourceRecord>
               ...
            </ResourceRecords>
            <GeoProximityLocation>
                <Coordinates>
                   <Latitude>decimal latitude</Latitude>
                   <Longitude>decimal longitude</Longitude>
                </Coordinates>
               <Bias>Integer bias</Bias>
             </GeoProximityLocation>
            <HealthCheckId>ID of a Route 53 health check</HealthCheckId>
         </ResourceRecordSet>
      </Change>
      ...
   </Changes>
</ChangeBatch>
</ChangeResourceRecordSetsRequest>
```

### Geoproximity Alias Syntax when using coordinates
<a name="API_ChangeResourceRecordSets_Example_8"></a>

For more information, see the following topics in the *Amazon Route 53 Developer Guide*:
+  [Geoproximity Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-geoproximity)
+  [Choosing Between Alias and Non-Alias Resource Record Sets](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html)

```
POST /2013-04-01/hostedzone/Route 53 hosted zone ID/rrset HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ChangeResourceRecordSetsRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
<ChangeBatch>
   <Comment>optional comment about the changes in this
      change batch request</Comment>
   <Changes>
      <Change>
         <Action>CREATE | DELETE | UPSERT</Action>
         <ResourceRecordSet>
            <Name>fully qualified domain name</Name>
            <Type>DNS record type</Type>
            <SetIdentifier>unique description for this resource record set</SetIdentifier>
            <AliasTarget>
               <HostedZoneId>hosted zone ID for your AWS resource or Route 53 hosted zone</HostedZoneId>
               <DNSName>DNS domain name for your AWS resource or another resource record set in this hosted zone</DNSName>
               <EvaluateTargetHealth>true | false</EvaluateTargetHealth>
            </AliasTarget>
            <GeoProximityLocation>
                <Coordinates>
                   <Latitude>decimal latitude</Latitude>
                   <Longitude>decimal longitude</Longitude>
                </Coordinates>
                <Bias>Integer bias</Bias>
             </GeoProximityLocation>
            <HealthCheckId>ID of a Route 53 health check</HealthCheckId>
         </ResourceRecordSet>
      </Change>
      ...
   </Changes>
</ChangeBatch>
</ChangeResourceRecordSetsRequest>
```

### Geoproximity Syntax when using an Region.
<a name="API_ChangeResourceRecordSets_Example_9"></a>

For more information, see [Geoproximity Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-geoproximity) in the *Amazon Route 53 Developer Guide*.

```
POST /2013-04-01/hostedzone/Route 53 hosted zone ID/rrset HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ChangeResourceRecordSetsRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
<ChangeBatch>
   <Comment>optional comment about the changes in this change batch request</Comment>
   <Changes>
      <Change>
         <Action>CREATE | DELETE | UPSERT</Action>
         <ResourceRecordSet>
           <Name>fully qualified domain name</Name>
            <Type>DNS record type</Type>
            <SetIdentifier>unique description for this resource record set</SetIdentifier>
            <TTL>time to live in seconds</TTL>
           <ResourceRecords>
               <ResourceRecord>
                  <Value>applicable value for the record type</Value>
               </ResourceRecord>
               ...
            </ResourceRecords>
            <GeoProximityLocation>
                <AWSRegion>Amazon EC2 region name</AWSRegion>
               <Bias>Integer bias</Bias>
             </GeoProximityLocation>
            <HealthCheckId>ID of a Route 53 health check</HealthCheckId>
         </ResourceRecordSet>
      </Change>
      ...
   </Changes>
</ChangeBatch>
</ChangeResourceRecordSetsRequest>
```

### Geoproximity Alias Syntax when using an Region
<a name="API_ChangeResourceRecordSets_Example_10"></a>

For more information, see the following topics in the *Amazon Route 53 Developer Guide*:
+  [Geoproximity Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-geoproximity)
+  [Choosing Between Alias and Non-Alias Resource Record Sets](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html)

```
POST /2013-04-01/hostedzone/Route 53 hosted zone ID/rrset HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ChangeResourceRecordSetsRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
<ChangeBatch>
   <Comment>optional comment about the changes in this
      change batch request</Comment>
   <Changes>
      <Change>
         <Action>CREATE | DELETE | UPSERT</Action>
         <ResourceRecordSet>
            <Name>fully qualified domain name</Name>
            <Type>DNS record type</Type>
            <etIdentifier>unique description for this resource record set</SetIdentifier>
            <AliasTarget>
               <HostedZoneId>hosted zone ID for your AWS resource or Route 53 hosted zone</HostedZoneId>
               <DNSName>DNS domain name for your AWS resource or another resource record set in this hosted zone</DNSName>
               <EvaluateTargetHealth>true | false</EvaluateTargetHealth>
            </AliasTarget>
            <GeoProximityLocation>
                 <AWSRegion>Amazon EC2 region name</AWSRegion>
                <Bias>Integer bias</Bias>
             </GeoProximityLocation>
            <HealthCheckId>ID of a Route 53 health check</HealthCheckId>
         </ResourceRecordSet>
      </Change>
      ...
   </Changes>
</ChangeBatch>
</ChangeResourceRecordSetsRequest>
```

### Geoproximity Syntax when using Local Zone Group.
<a name="API_ChangeResourceRecordSets_Example_11"></a>

For more information, see [Geoproximity Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-geoproximity) in the *Amazon Route 53 Developer Guide*.

```
POST /2013-04-01/hostedzone/Route 53 hosted zone ID/rrset HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ChangeResourceRecordSetsRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
<ChangeBatch>
   <Comment>optional comment about the changes in this change batch request</Comment>
   <Changes>
      <Change>
         <Action>CREATE | DELETE | UPSERT</Action>
         <ResourceRecordSet>
           <Name>fully qualified domain name</Name>
            <Type>DNS record type</Type>
            <SetIdentifier>unique description for this resource record set</SetIdentifier>
            <TTL>time to live in seconds</TTL>
           <ResourceRecords>
               <ResourceRecord>
                  <Value>applicable value for the record type</Value>
               </ResourceRecord>
               ...
            </ResourceRecords>
            <GeoProximityLocation>
                <LocalZoneGroup>Amazon EC2 local zone group name</LocalZoneGroup>
               <Bias>Integer bias</Bias>
             </GeoProximityLocation>
            <HealthCheckId>ID of a Route 53 health check</HealthCheckId>
         </ResourceRecordSet>
      </Change>
      ...
   </Changes>
</ChangeBatch>
</ChangeResourceRecordSetsRequest>
```

### Geoproximity Alias Syntax when using a Local Zone Group
<a name="API_ChangeResourceRecordSets_Example_12"></a>

For more information, see the following topics in the *Amazon Route 53 Developer Guide*:
+  [Geoproximity Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-geoproximity)
+  [Choosing Between Alias and Non-Alias Resource Record Sets](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html)

```
POST /2013-04-01/hostedzone/Route 53 hosted zone ID/rrset HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ChangeResourceRecordSetsRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
<ChangeBatch>
   <Comment>optional comment about the changes in this
      change batch request</Comment>
   <Changes>
      <Change>
         <Action>CREATE | DELETE | UPSERT</Action>
         <ResourceRecordSet>
            <Name>fully qualified domain name</Name>
            <Type>DNS record type</Type>
            <etIdentifier>unique description for this resource record set</SetIdentifier>
            <AliasTarget>
               <HostedZoneId>hosted zone ID for your AWS resource or Route 53 hosted zone</HostedZoneId>
               <DNSName>DNS domain name for your AWS resource or another resource record set in this hosted zone</DNSName>
               <EvaluateTargetHealth>true | false</EvaluateTargetHealth>
            </AliasTarget>
            <GeoProximityLocation>
                <LocalZoneGroup>Amazon EC2 local zone group name</LocalZoneGroup>
                <Bias>Integer bias</Bias>
             </GeoProximityLocation>
            <HealthCheckId>ID of a Route 53 health check</HealthCheckId>
         </ResourceRecordSet>
      </Change>
      ...
   </Changes>
</ChangeBatch>
</ChangeResourceRecordSetsRequest>
```

### IP-based routing Syntax
<a name="API_ChangeResourceRecordSets_Example_13"></a>

For more information, see [IP-based routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-ipbased) in the *Amazon Route 53 Developer Guide*.

```
POST /2013-04-01/hostedzone/Route 53 hosted zone ID/rrset HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ChangeResourceRecordSetsRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
<ChangeBatch>
   <Comment>optional comment about the changes in this
      change batch request</Comment>
   <Changes>
      <Change>
         <Action>CREATE | DELETE | UPSERT</Action>
         <ResourceRecordSet>
            <Name>fully qualified domain name</Name>
            <Type>DNS record type</Type>
            <SetIdentifier>unique description for this resource record set</SetIdentifier>
            <TTL>time to live in seconds</TTL>
            <ResourceRecords>
               <ResourceRecord>
                  <Value>applicable value for the record type</Value>
               </ResourceRecord>
               ...
            </ResourceRecords>
            <CidrRoutingConfig>
               <CollectionId>CIDR collection ID</CollectionId>
               <LocationName>CIDR collection location name</LocationName>
            </CidrRoutingConfig>
            <HealthCheckId>ID of a Route 53 health check</HealthCheckId>
         </ResourceRecordSet>
      </Change>
      ...
   </Changes>
</ChangeBatch>
</ChangeResourceRecordSetsRequest>
```

### IP-based Alias Syntax
<a name="API_ChangeResourceRecordSets_Example_14"></a>

For more information, see the following topics in the *Amazon Route 53 Developer Guide*:
+  [IP-based routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-ipbased)
+  [Choosing Between Alias and Non-Alias Resource Record Sets](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html)

```
POST /2013-04-01/hostedzone/Route 53 hosted zone ID/rrset HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ChangeResourceRecordSetsRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
<ChangeBatch>
   <Comment>optional comment about the changes in this
      change batch request</Comment>
   <Changes>
      <Change>
         <Action>CREATE | DELETE | UPSERT</Action>
         <ResourceRecordSet>
            <Name>fully qualified domain name</Name>
            <Type>DNS record type</Type>
            <SetIdentifier>unique description for this resource record set</SetIdentifier>

            <AliasTarget>
               <HostedZoneId>hosted zone ID for your AWS resource or Route 53 hosted zone</HostedZoneId>
               <DNSName>DNS domain name for your AWS resource or another resource record set in this hosted zone</DNSName>
               <EvaluateTargetHealth>true | false</EvaluateTargetHealth>
            </AliasTarget>
            <CidrRoutingConfig>
               <CollectionId>CIDR collection ID</CollectionId>
               <LocationName>CIDR collection location name</LocationName>
            </CidrRoutingConfig>
            <HealthCheckId>optional ID of a Route 53 health check</HealthCheckId>
         </ResourceRecordSet>
      </Change>
      ...
   </Changes>
</ChangeBatch>
</ChangeResourceRecordSetsRequest>
```

### Latency Resource Record Set Syntax
<a name="API_ChangeResourceRecordSets_Example_15"></a>

For information about latency resource record sets, see [Latency-Based Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency) in the *Amazon Route 53 Developer Guide*.

```
POST /2013-04-01/hostedzone/Route 53 hosted zone ID/rrset HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ChangeResourceRecordSetsRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
<ChangeBatch>
   <Comment>optional comment about the changes in this change batch request</Comment>
   <Changes>
      <Change>
         <Action>CREATE | DELETE | UPSERT</Action>
         <ResourceRecordSet>
            <Name>fully qualified domain name</Name>
            <Type>DNS record type</Type>
            <SetIdentifier>unique description for this resource record set</SetIdentifier>
            <Region>Amazon EC2 region name</Region>
            <TTL>time to live in seconds</TTL>
            <ResourceRecords>
               <ResourceRecord>
                  <Value>applicable value for the record type</Value>
               </ResourceRecord>
               ...
            </ResourceRecords>
            <HealthCheckId>optional ID of a Route 53 health check</HealthCheckId>
         </ResourceRecordSet>
      </Change>
      ...
   </Changes>
</ChangeBatch>
</ChangeResourceRecordSetsRequest>
```

### Latency Alias Resource Record Set Syntax
<a name="API_ChangeResourceRecordSets_Example_16"></a>

For information about latency resource record sets, see [Latency-Based Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency) in the *Amazon Route 53 Developer Guide*. For information about alias resource record sets, see [Choosing Between Alias and Non-Alias Resource Record Sets](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html) in the *Amazon Route 53 Developer Guide*.

```
POST /2013-04-01/hostedzone/Route 53 hosted zone ID/rrset HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ChangeResourceRecordSetsRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
<ChangeBatch>
   <Comment>optional comment about the changes in this change batch request</Comment>
   <Changes>
      <Change>
         <Action>CREATE | DELETE | UPSERT</Action>
         <ResourceRecordSet>
            <Name>fully qualified domain name</Name>
            <Type>DNS record type</Type>
            <SetIdentifier>unique description for this resource record set</SetIdentifier>
            <Region>Amazon EC2 region name</Region>
            <AliasTarget>
               <HostedZoneId>hosted zone ID for your AWS resource or Route 53 hosted zone</HostedZoneId>
               <DNSName>DNS domain name for your AWS resource or another resource record set in this hosted zone</DNSName>
               <EvaluateTargetHealth>true | false</EvaluateTargetHealth>
            </AliasTarget>
            <HealthCheckId>optional ID of a Route 53 health check</HealthCheckId>
         </ResourceRecordSet>
      </Change>
      ...
   </Changes>
</ChangeBatch>
</ChangeResourceRecordSetsRequest>
```

### Multivalue Answer Syntax
<a name="API_ChangeResourceRecordSets_Example_17"></a>

This example illustrates one usage of ChangeResourceRecordSets.

```
POST /2013-04-01/hostedzone/Route 53 hosted zone ID/rrset HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ChangeResourceRecordSetsRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
<ChangeBatch>
   <Comment>optional comment about the changes in this change batch request</Comment>
   <Changes>
      <Change>
         <Action>CREATE | DELETE | UPSERT</Action>
         <ResourceRecordSet>
            <Name>fully qualified domain name</Name>
            <Type>DNS record type</Type>
            <TTL>time to live in seconds</TTL>
            <SetIdentifier>unique description for this resource record set</SetIdentifier>
            <ResourceRecords>
               <ResourceRecord>
                  <Value>applicable value for the record type</Value>
               </ResourceRecord>
               ...
            </ResourceRecords>
            <MultiValueAnswer>true</MultiValueAnswer>
            <HealthCheckId>optional ID of a Route 53 health check</HealthCheckId>
         </ResourceRecordSet>
      </Change>
      ...
   </Changes>
</ChangeBatch>
</ChangeResourceRecordSetsRequest>
```

### Weighted Resource Record Set Syntax
<a name="API_ChangeResourceRecordSets_Example_18"></a>

For information about weighted resource record sets, see [Weighted Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted) in the *Amazon Route 53 Developer Guide*.

```
POST /2013-04-01/hostedzone/Route 53 hosted zone ID/rrset HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ChangeResourceRecordSetsRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
<ChangeBatch>
   <Comment>optional comment about the changes in this change batch request</Comment>
   <Changes>
      <Change>
         <Action>CREATE | DELETE | UPSERT</Action>
         <ResourceRecordSet>
            <Name>fully qualified domain name</Name>
            <Type>DNS record type</Type>
            <SetIdentifier>unique description for this resource record set</SetIdentifier>
            <Weight>value between 0 and 255</Weight>
            <TTL>time to live in seconds</TTL>
            <ResourceRecords>
               <ResourceRecord>
                  <Value>applicable value for the record type</Value>
               </ResourceRecord>
               ...
            </ResourceRecords>
            <HealthCheckId>optional ID of a Route 53 health check</HealthCheckId>
         </ResourceRecordSet>
      </Change>
      ...
   </Changes>
</ChangeBatch>
</ChangeResourceRecordSetsRequest>
```

### Weighted Alias Resource Record Set Syntax
<a name="API_ChangeResourceRecordSets_Example_19"></a>

For information about weighted resource record sets, see [Weighted Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-weighted) in the *Amazon Route 53 Developer Guide*. For information about alias resource record sets, see [Choosing Between Alias and Non-Alias Resource Record Sets](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html) in the *Amazon Route 53 Developer Guide*.

```
POST /2013-04-01/hostedzone/Route 53 hosted zone ID/rrset HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ChangeResourceRecordSetsRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
<ChangeBatch>
   <Comment>optional comment about the changes in this change batch request</Comment>
   <Changes>
      <Change>
         <Action>CREATE | DELETE | UPSERT</Action>
         <ResourceRecordSet>
            <Name>fully qualified domain name</Name>
            <Type>DNS record type</Type>
            <SetIdentifier>unique description for this resource record set</SetIdentifier>
            <Weight>value between 0 and 255</Weight>
            <AliasTarget>
               <HostedZoneId>hosted zone ID for your AWS resource or Route 53 hosted zone</HostedZoneId>
               <DNSName>DNS domain name for your AWS resource or another resource record set in this hosted zone</DNSName>
               <EvaluateTargetHealth>true | false</EvaluateTargetHealth>
            </AliasTarget>
            <HealthCheckId>optional ID of a Route 53 health check</HealthCheckId>
         </ResourceRecordSet>
      </Change>
      ...
   </Changes>
</ChangeBatch>
</ChangeResourceRecordSetsRequest>
```

## See Also
<a name="API_ChangeResourceRecordSets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/ChangeResourceRecordSets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/ChangeResourceRecordSets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ChangeResourceRecordSets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/ChangeResourceRecordSets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ChangeResourceRecordSets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/ChangeResourceRecordSets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/ChangeResourceRecordSets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/ChangeResourceRecordSets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/ChangeResourceRecordSets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ChangeResourceRecordSets)
