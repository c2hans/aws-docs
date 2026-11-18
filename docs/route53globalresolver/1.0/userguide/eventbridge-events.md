---
source_url: https://docs.aws.amazon.com/route53globalresolver/1.0/userguide/eventbridge-events.html
---

# EventBridge events for Amazon Route 53 Global Resolver automation and monitoring
<a name="eventbridge-events"></a>

You can monitor Amazon Route 53 Global Resolver events in EventBridge, which delivers a stream of real-time data from your own applications, software-as-a-service (SaaS) applications, and AWS services. EventBridge routes that data to targets such as Lambda and Amazon SNS. These events are the same as those that appear in CloudWatch Events, which delivers a near real-time stream of system events that describe changes in AWS resources.

The following examples show events for Amazon Route 53 Global Resolver.

## Amazon Route 53 Global Resolver state change event
<a name="global-resolver-state-change-event"></a>

This event is generated when a global resolver changes state, such as when it becomes operational or encounters an error.

```
{
   "version": "0",
   "id": "01234567-EXAMPLE",
   "detail-type": "Route53 Global Resolver State Change",
   "source": "aws.route53globalresolver",
   "account": "123456789012",
   "time": "2025-03-15T10:23:43Z",
   "region": "us-east-1",
   "resources": [
     "arn:aws:route53globalresolver::123456789012:global-resolver/gr-123abc456"
   ],
   "detail": {
     "event": "stateChange",
     "globalResolverId": "gr-123abc456",
     "previousState": "CREATING",
     "currentState": "OPERATIONAL",
     "stateChangeReason": "Global resolver successfully created"
   }
}
```

## DNS View state change event
<a name="dns-view-state-change-event"></a>

This event is generated when a DNS view changes state or configuration.

```
{
   "version": "0",
   "id": "01234567-EXAMPLE",
   "detail-type": "Route53 Global Resolver DNS View State Change",
   "source": "aws.route53globalresolver",
   "account": "123456789012",
   "time": "2025-03-15T10:25:12Z",
   "region": "us-east-1",
   "resources": [
     "arn:aws:route53globalresolver::123456789012:dns-view/dnsv-456pqr789"
   ],
   "detail": {
     "event": "stateChange",
     "dnsViewId": "dnsv-456pqr789",
     "globalResolverId": "gr-123abc456",
     "previousState": "UPDATING",
     "currentState": "OPERATIONAL",
     "stateChangeReason": "DNS view configuration updated successfully"
   }
}
```
