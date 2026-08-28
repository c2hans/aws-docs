---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_Event.html
---

# Event
<a name="API_Event"></a>

Log entry describing an event that involves Amazon GameLift Servers resources (such as a fleet). In addition to tracking activity, event codes and messages can provide additional information for troubleshooting and debugging problems.

## Contents
<a name="API_Event_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Count **   <a name="gameliftservers-Type-Event-Count"></a>
The number of times that this event occurred.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 101.
Required: No

 ** EventCode **   <a name="gameliftservers-Type-Event-EventCode"></a>
The type of event being logged.
 **Fleet state transition events:**
+ FLEET\_CREATED -- A fleet resource was successfully created with a status of `NEW`. Event messaging includes the fleet ID.
+ FLEET\_STATE\_DOWNLOADING -- Fleet status changed from `NEW` to `DOWNLOADING`. Amazon GameLift Servers is downloading the compressed build and running install scripts.
+ FLEET\_STATE\_VALIDATING -- Fleet status changed from `DOWNLOADING` to `VALIDATING`. Amazon GameLift Servers has successfully installed build and is now validating the build files.
+ FLEET\_STATE\_BUILDING -- Fleet status changed from `VALIDATING` to `BUILDING`. Amazon GameLift Servers has successfully verified the build files and is now launching a fleet instance.
+ FLEET\_STATE\_ACTIVATING -- Fleet status changed from `BUILDING` to `ACTIVATING`. Amazon GameLift Servers is launching a game server process on the fleet instance and is testing its connectivity with the Amazon GameLift Servers service.
+ FLEET\_STATE\_ACTIVE -- The fleet's status changed from `ACTIVATING` to `ACTIVE`. The fleet is now ready to host game sessions.
+ FLEET\_STATE\_ERROR -- The Fleet's status changed to `ERROR`. Describe the fleet event message for more details.
 **Fleet creation events (ordered by fleet creation activity):**
+ FLEET\_BINARY\_DOWNLOAD\_FAILED -- The build failed to download to the fleet instance.
+ FLEET\_CREATION\_EXTRACTING\_BUILD -- The game server build was successfully downloaded to an instance, and Amazon GameLift Serversis now extracting the build files from the uploaded build. Failure at this stage prevents a fleet from moving to ACTIVE status. Logs for this stage display a list of the files that are extracted and saved on the instance. Access the logs by using the URL in *PreSignedLogUrl*.
+ FLEET\_CREATION\_RUNNING\_INSTALLER -- The game server build files were successfully extracted, and Amazon GameLift Servers is now running the build's install script (if one is included). Failure in this stage prevents a fleet from moving to ACTIVE status. Logs for this stage list the installation steps and whether or not the install completed successfully. Access the logs by using the URL in *PreSignedLogUrl*.
+ FLEET\_CREATION\_COMPLETED\_INSTALLER -- The game server build files were successfully installed and validation of the installation will begin soon.
+ FLEET\_CREATION\_FAILED\_INSTALLER -- The installed failed while attempting to install the build files. This event indicates that the failure occurred before Amazon GameLift Servers could start validation.
+ FLEET\_CREATION\_VALIDATING\_RUNTIME\_CONFIG -- The build process was successful, and the GameLift is now verifying that the game server launch paths, which are specified in the fleet's runtime configuration, exist. If any listed launch path exists, Amazon GameLift Servers tries to launch a game server process and waits for the process to report ready. Failures in this stage prevent a fleet from moving to `ACTIVE` status. Logs for this stage list the launch paths in the runtime configuration and indicate whether each is found. Access the logs by using the URL in *PreSignedLogUrl*.
+ FLEET\_VALIDATION\_LAUNCH\_PATH\_NOT\_FOUND -- Validation of the runtime configuration failed because the executable specified in a launch path does not exist on the instance.
+ FLEET\_VALIDATION\_EXECUTABLE\_RUNTIME\_FAILURE -- Validation of the runtime configuration failed because the executable specified in a launch path failed to run on the fleet instance.
+ FLEET\_VALIDATION\_TIMED\_OUT -- Validation of the fleet at the end of creation timed out. Try fleet creation again.
+ FLEET\_ACTIVATION\_FAILED -- The fleet failed to successfully complete one of the steps in the fleet activation process. This event code indicates that the game build was successfully downloaded to a fleet instance, built, and validated, but was not able to start a server process. For more information, see [Debug Fleet Creation Issues](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-debug.html#fleets-creating-debug-creation).
+ FLEET\_ACTIVATION\_FAILED\_NO\_INSTANCES -- Fleet creation was not able to obtain any instances based on the input fleet attributes. Try again at a different time or choose a different combination of fleet attributes such as fleet type, instance type, etc.
+ FLEET\_INITIALIZATION\_FAILED -- A generic exception occurred during fleet creation. Describe the fleet event message for more details.
 **VPC peering events:**
+ FLEET\_VPC\_PEERING\_SUCCEEDED -- A VPC peering connection has been established between the VPC for an Amazon GameLift Servers fleet and a VPC in your AWS account.
+ FLEET\_VPC\_PEERING\_FAILED -- A requested VPC peering connection has failed. Event details and status information provide additional detail. A common reason for peering failure is that the two VPCs have overlapping CIDR blocks of IPv4 addresses. To resolve this, change the CIDR block for the VPC in your AWS account. For more information on VPC peering failures, see [https://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide/invalid-peering-configurations.html](https://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide/invalid-peering-configurations.html)
+ FLEET\_VPC\_PEERING\_DELETED -- A VPC peering connection has been successfully deleted.
 **Spot instance events:**
+  INSTANCE\_INTERRUPTED -- A spot instance was interrupted by EC2 with a two-minute notification.
+ INSTANCE\_RECYCLED -- A spot instance was determined to have a high risk of interruption and is scheduled to be recycled once it has no active game sessions.
 **Server process events:**
+ SERVER\_PROCESS\_INVALID\_PATH -- The game server executable or script could not be found based on the Fleet runtime configuration. Check that the launch path is correct based on the operating system of the Fleet.
+ SERVER\_PROCESS\_SDK\_INITIALIZATION\_TIMEOUT -- The server process did not call `InitSDK()` within the time expected (5 minutes). Check your game session log to see why `InitSDK()` was not called in time. This event is not emitted for managed container fleets and Anywhere fleets unless they're deployed with the Amazon GameLift Servers Agent.
+ SERVER\_PROCESS\_PROCESS\_READY\_TIMEOUT -- The server process did not call `ProcessReady()` within the time expected (5 minutes) after calling `InitSDK()`. Check your game session log to see why `ProcessReady()` was not called in time.
+ SERVER\_PROCESS\_CRASHED -- The server process exited without calling `ProcessEnding()`. Check your game session log to see why `ProcessEnding()` was not called.
+ SERVER\_PROCESS\_TERMINATED\_UNHEALTHY -- The server process did not report a valid health check for too long and was therefore terminated by GameLift. Check your game session log to see if the thread became stuck processing a synchronous task for too long.
+ SERVER\_PROCESS\_FORCE\_TERMINATED -- The server process did not exit cleanly within the time expected after `OnProcessTerminate()` was sent. Check your game session log to see why termination took longer than expected.
+ SERVER\_PROCESS\_PROCESS\_EXIT\_TIMEOUT -- The server process did not exit cleanly within the time expected (30 seconds) after calling `ProcessEnding()`. Check your game session log to see why termination took longer than expected.
 **Game session events:**
+ GAME\_SESSION\_ACTIVATION\_TIMEOUT -- GameSession failed to activate within the expected time. Check your game session log to see why `ActivateGameSession()` took longer to complete than expected.
 **Other fleet events:**
+ FLEET\_SCALING\_EVENT -- A change was made to the fleet's capacity settings (desired instances, minimum/maximum scaling limits). Event messaging includes the new capacity settings.
+ FLEET\_NEW\_GAME\_SESSION\_PROTECTION\_POLICY\_UPDATED -- A change was made to the fleet's game session protection policy setting. Event messaging includes both the old and new policy setting.
+ FLEET\_DELETED -- A request to delete a fleet was initiated.
+ FLEET\_EXPIRED -- The fleet has been expired. The fleet is scaled down to zero instances and can no longer host game sessions.
+  GENERIC\_EVENT -- An unspecified event has occurred.
Type: String
Valid Values: `GENERIC_EVENT | FLEET_CREATED | FLEET_DELETED | FLEET_SCALING_EVENT | FLEET_STATE_DOWNLOADING | FLEET_STATE_VALIDATING | FLEET_STATE_BUILDING | FLEET_STATE_ACTIVATING | FLEET_STATE_ACTIVE | FLEET_STATE_ERROR | FLEET_STATE_PENDING | FLEET_STATE_CREATING | FLEET_STATE_CREATED | FLEET_STATE_UPDATING | FLEET_INITIALIZATION_FAILED | FLEET_BINARY_DOWNLOAD_FAILED | FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND | FLEET_VALIDATION_EXECUTABLE_RUNTIME_FAILURE | FLEET_VALIDATION_TIMED_OUT | FLEET_ACTIVATION_FAILED | FLEET_ACTIVATION_FAILED_NO_INSTANCES | FLEET_NEW_GAME_SESSION_PROTECTION_POLICY_UPDATED | SERVER_PROCESS_INVALID_PATH | SERVER_PROCESS_SDK_INITIALIZATION_TIMEOUT | SERVER_PROCESS_PROCESS_READY_TIMEOUT | SERVER_PROCESS_CRASHED | SERVER_PROCESS_TERMINATED_UNHEALTHY | SERVER_PROCESS_FORCE_TERMINATED | SERVER_PROCESS_PROCESS_EXIT_TIMEOUT | SERVER_PROCESS_SDK_INITIALIZATION_FAILED | SERVER_PROCESS_MISCONFIGURED_CONTAINER_PORT | GAME_SESSION_ACTIVATION_TIMEOUT | FLEET_CREATION_EXTRACTING_BUILD | FLEET_CREATION_RUNNING_INSTALLER | FLEET_CREATION_VALIDATING_RUNTIME_CONFIG | FLEET_VPC_PEERING_SUCCEEDED | FLEET_VPC_PEERING_FAILED | FLEET_VPC_PEERING_DELETED | INSTANCE_INTERRUPTED | INSTANCE_RECYCLED | INSTANCE_REPLACED_UNHEALTHY | FLEET_CREATION_COMPLETED_INSTALLER | FLEET_CREATION_FAILED_INSTALLER | COMPUTE_LOG_UPLOAD_FAILED | GAME_SERVER_CONTAINER_GROUP_CRASHED | PER_INSTANCE_CONTAINER_GROUP_CRASHED | GAME_SERVER_CONTAINER_GROUP_REPLACED_UNHEALTHY | LOCATION_STATE_PENDING | LOCATION_STATE_CREATING | LOCATION_STATE_CREATED | LOCATION_STATE_ACTIVATING | LOCATION_STATE_ACTIVE | LOCATION_STATE_UPDATING | LOCATION_STATE_ERROR | LOCATION_STATE_DELETING | LOCATION_STATE_DELETED`
Required: No

 ** EventId **   <a name="gameliftservers-Type-Event-EventId"></a>
A unique identifier for a fleet event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** EventTime **   <a name="gameliftservers-Type-Event-EventTime"></a>
Time stamp indicating when this event occurred. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).
Type: Timestamp
Required: No

 ** Message **   <a name="gameliftservers-Type-Event-Message"></a>
Additional information related to the event.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** PreSignedLogUrl **   <a name="gameliftservers-Type-Event-PreSignedLogUrl"></a>
Location of stored logs with additional detail that is related to the event. This is useful for debugging issues. The URL is valid for 15 minutes. You can also access fleet creation logs through the Amazon GameLift Servers console.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** ResourceId **   <a name="gameliftservers-Type-Event-ResourceId"></a>
A unique identifier for an event resource, such as a fleet ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_Event_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/Event)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/Event)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/Event)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
