---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/reference.html
---

# Reference
<a name="reference"></a>

This section includes information about an optional feature for collecting unique metrics for this solution and a [list of Amazon staff](#contributors) who contributed to this solution.

## Data collection
<a name="data-collection"></a>

This solution sends operational metrics to AWS (the "Data") about the use of this solution. We use this Data to better understand how customers use this solution and related services and products. AWS’s collection of this Data is subject to the [AWS Privacy Notice](https://aws.amazon.com/privacy/).

The following information is collected and sent to AWS:
+ Hub Account ID
+ Lease Approved Events
  + Maximum budget amount configured for the lease
  + Lease duration in hours
  + Whether the lease was automatically approved or required manual approval
  + Creation method (indicates whether lease was created via user request or manager assignment)
+ Account Cleanup Events
  + Number of accounts successfully cleaned (based on Step Function success metrics)
  + Duration of failed account cleanup attempts
  + Duration of successful account cleanup attempts
+ Lease Terminated Events
  + Maximum budget amount that was configured for the lease
  + Actual amount spent during the lease period
  + Maximum duration that was configured for the lease
  + Actual duration the lease was active
  + Reason for lease termination (expired, manually terminated, budget exceeded, etc.)
+ LeaseUnfrozen
  + Total number of leases unfrozen
  + Frequency of unfreeze events per individual lease
+ Spend Monitoring (monthly heartbeat — 4th of every month)
  + Total cost of all sandbox accounts
  + Total operational cost of running the solution infrastructure
+ Deployment Summary (daily heartbeat)
  + Total number of lease templates configured
  + Number of public lease templates (visible to all users)
  + Number of private lease templates (visible only to administrators and managers)
  + Number of leases created by managers on behalf of users
  + Number of leases created by users through self-service requests
  + Number of accounts available in the account pool
  + Number of accounts currently active with leases
  + Number of accounts in frozen state
  + Number of accounts undergoing cleanup process
  + Number of accounts in quarantine state requiring manual intervention

## Contributors
<a name="contributors"></a>
+ Wayne Soutter
+ Chris Ellis
+ Rakshana Balakrishnan
+ Nils de Vries
+ Emma Arrigo
+ Claudia Woods
+ Joan Morgan
+ Todd Gruet
+ Shu Jackson
+ Celia Ng
+ Rainer Moeller
+ Lalit Grover
+ Kevin Hargita
+ Caleb Pearson
+ Abe Wubshet
+ Adrian Tadros
+ Sanjay Reddy Kandi
+ Vincent Rioux
+ Swapnil Ogale
+ Elie Elmalem
+ Patrick Quinlan
