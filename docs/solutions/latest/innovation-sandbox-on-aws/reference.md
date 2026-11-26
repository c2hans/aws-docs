---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/reference.html
---

# Reference

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
  + For leases that reached their maximum budget, which check detected it (hourly lease monitoring or Amazon Bedrock token monitoring) and the cost it reported
+ Budget Threshold Fired Events (for each budget threshold reached)
  + Threshold amount, action, cost basis, and which check evaluated it (hourly lease monitoring or Amazon Bedrock token monitoring)
  + Current, reported, and estimated cost at that time, and hours since the latest AWS Cost Explorer reading
  + For freeze thresholds, the cost used for the freeze decision
+ Spend Rate Threshold Fired Events (for each spend rate threshold reached)
  + Rate period, threshold rate, measured rate, action, and which check evaluated it
  + Current, reported, and estimated cost at that time, and hours since the latest AWS Cost Explorer reading
  + For freeze thresholds, the cost used for the freeze decision
+ Projection Accuracy Events (when a new AWS Cost Explorer reading arrives for a lease with estimated cost tracking)
  + Estimated cost, the new reported cost, and the difference in USD and as a percentage
  + Hours between readings, the rate period, and the estimation method version
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
  + Number of permission sets in the cached catalog, including the built-in user permission set
  + Number of stored assignments using a custom permission set across all leases
  + Number of active or frozen leases with a custom permission set selected for at least one assignment
  + Average and maximum number of distinct permission sets selected per active or frozen lease
  + Average and maximum number of allowed permission sets per lease template and per active or frozen lease
  + Whether **Allow estimated cost tracking**, **Allow Bedrock token monitoring**, and **Enable service cost breakdown** are turned on
  + Number of lease templates and Active leases with estimated cost tracking turned on, and how many of them have spend rate thresholds
  + Number of lease templates and Active leases with Amazon Bedrock token monitoring turned on
  + Whether email notifications through Amazon SES are enabled
  + Whether the Amazon SNS integration topic is enabled
  + Whether email is sent through a delegated SES identity in another account
  + Number of confirmed subscriptions to the SNS integration topic
  + Number of notification delivery failures for SES and for SNS

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
