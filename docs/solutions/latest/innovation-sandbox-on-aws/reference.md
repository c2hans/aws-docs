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
  + Number of principals specified for the lease at publish time
+ Account Cleanup Events
  + Number of accounts successfully cleaned (based on Step Function success metrics)
  + Duration of failed account cleanup attempts
  + Duration of successful account cleanup attempts
  + Number of IAM Identity Center account assignments found and removed during cleanup
  + Number of internal assignment records found and removed during cleanup
+ Account Quarantined Events
  + Reason for account quarantine (manual administrator action, detected account drift, or failed account cleanup)
+ Lease Terminated Events
  + Maximum budget amount that was configured for the lease
  + Actual amount spent during the lease period
  + Maximum duration that was configured for the lease
  + Actual duration the lease was active
  + Reason for lease termination (expired, manually terminated, budget exceeded, etc.)
+ LeaseUnfrozen
  + Total number of leases unfrozen
  + Frequency of unfreeze events per individual lease
+ Lease Assignment Events (lease sharing)
  + The lifecycle action that triggered assignment processing (one of: UPDATE, PUBLISH, FREEZE, UNFREEZE, or TERMINATE)
  + Number of principals (users and groups) processed in the operation
  + Number of principal assignments that succeeded and the number that failed
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
  + Whether a maximum lease duration is required for lease templates
  + Whether users are permitted to terminate their own leases
  + Lease request rate limit window, in hours
  + Maximum number of lease requests allowed per rate limit window
  + Number of lease templates that allow lease owners to share leases
  + Number of leases shared with additional users or groups
  + Total number of user assignments and total number of group assignments across all leases
  + Average and maximum number of assignments per shared lease
  + Whether the lease sharing feature is enabled globally
  + Whether principal search is enabled

## Contributors
<a name="contributors"></a>
+ Abe Wubshet
+ Adrian Tadros
+ Alex Sieber
+ Caleb Pearson
+ Celia Ng
+ Chris Ellis
+ Claudia Woods
+ Elie Elmalem
+ Emma Arrigo
+ Joan Morgan
+ Johanna Wood
+ Kevin Hargita
+ Lalit Grover
+ Manish Jangid
+ Nils de Vries
+ Patrick Quinlan
+ Peter DeVries
+ Rainer Moeller
+ Rakshana Balakrishnan
+ Sanjay Reddy Kandi
+ Shu Jackson
+ Swapnil Ogale
+ Todd Gruet
+ Vincent Rioux
+ Wayne Soutter
+ Youngmin Son
