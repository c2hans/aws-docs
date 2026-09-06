---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration-connect/checklist.html
---

# Migration checklists
<a name="checklist"></a>

Use the following checklists to ensure that you complete important migration activities in the correct order.

## Before you go live
<a name="pre-checklist"></a>

1. Verify that the release passes user acceptance testing (UAT) and that any remaining issues have been accepted by stakeholders.

1. Plan the phone number cutover:
   + If you're using toll-free number service (TFNS): Verify that the service is ready to repoint to the Amazon Connect Customer queue phone number. This might be a self-service task or might require a ticket with the provider, so consider the lead time to complete this task.
   + If you're porting the number to AWS: File a number porting request ticket well before the target go-live date. (See *Number porting* in the [Best practices for migrations](tech-considerations.md) section earlier in this guide.)

1. Verify that end-users have been trained and know how to use the new platform.

1. Verify that the operations team has signed off on the new platform and has incorporated it into their support model. For example, the business as usual (BAU) team should be ready to manage any support tickets that are opened on the new platform.

1. Verify that the code base has been deployed to the production environment.
**Note**
This activity might require its own change request (CR), which would be submitted before and separately from the go-live CR for cutover.

1. Verify that the service lines that are in scope have successfully run UAT scripts by using a temporary phone number.

1. Submit a change request (CR) for go-live cutover and gain approval from the relevant change approval board (CAB). The evidence from this checklist is provided as input into the CAB discussion. The outcome of the CAB discussion is an approval to perform a cutover on a specific date and time.

## On the day you go live
<a name="go-live-checklist"></a>

1. Ensure that agents are logged in to Amazon Connect and are available to receive and make calls and participate in chats. Supervisors and operators can check agent activity by using real-time reports on the Amazon Connect dashboard.

1. Ensure that the post go-live support (PGLS) team is present and ready.

1. (Optional) Confirm that staff who can assist agents and help troubleshoot problems is in position (on-site or at remote help desk).

1. Ensure that BAU support teams are aware of the cutover time and are ready to handle any support tickets.
**Note**
   The PGLS team works alongside the BAU support teams.

1. Open a conference bridge for stakeholders to receive status updates. This bridge also serves as a forum to discuss any issues that might occur. Keep the bridge open until go-live (or rollback) activities have been completed successfully.

1. Initiate the cutover (for example, the TFNS repoint) at the approved time.

1. Review real-time metrics on the Amazon Connect dashboard to verify the following:
   + Calls are being answered.
   + Abandonment rates and average handle times (AHT) are as expected.
   + Queue depth remains sensible.
