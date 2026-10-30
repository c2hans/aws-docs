---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/static-stability.html
---

# Static stability
<a name="static-stability"></a>

 Although the data plane is logically separate from the control plane, it still depends on information and instructions provided by the control plane. This makes the control plane a dependency of the data plane. However, AWS services are intentionally designed so that data planes minimize availability impacts when their dependencies are impaired. In distributed systems, this property is commonly described as *graceful degradation*: when a dependency fails, the system continues to operate in a predictable, though potentially degraded, mode. This provides *stability*: users can continue to use existing data plane functionality even if management or configuration operations are unavailable.

 A second, equally important attribute of this component separation is that recovery itself is *static*. The data plane doesn’t attempt to dynamically make changes in response to failure. By deliberately avoiding dynamic changes, data planes don’t take control plane operations as a dependency for recovery. This reduces the risk of failed or incomplete recovery when those systems are themselves impaired. Systems that are preconfigured to tolerate failures, rather than dynamically responding to them, are more reliable because their behavior doesn’t change during failures.

 The combination of continued operation without dependency on the control plane for configuration information or recovery procedures is what we call *static stability*. In AWS, designing data planes to be statically stable allows us to decouple their availability from dependencies, including the control plane, and enforce strong fault isolation between them. This principle prioritizes predictable, reliable functionality to produce stable operations during failure. There are several architectural strategies we use to build statically stable data planes; the following patterns illustrate the most common approaches.

Independent startup
Circular dependencies can prevent each dependency from recovering during a failure. We design services to reach a running state, with potentially degraded capabilities, if its dependencies are unavailable during service start. After the dependencies come online, the service can return to full operational capability. This prevents the type of crash-loop failure where systems never recover.

Pre-provisioning
When impairments occur, such as the loss of power in an Availability Zone, this can cause resources to be unavailable, like Amazon EC2 instances. In this case, for a service deployed across three Availability Zones, losing a third of the fleet’s capacity can lead to overload. One approach to resolve that capacity loss would be to let [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) replace the lost instances. However, this creates a dependency on the Amazon EC2 control plane to launch new instances. To remove that dependency in the service’s recovery path, Amazon EC2 instances are pre-provisioned in the remaining AZs to absorb the load. This approach works for non-compute resources as well such as AWS accounts, Amazon S3 buckets, IAM roles, and Amazon SQS queues.

Maintain existing state
If state or configuration information is provided by a dependency, the service can choose to maintain the existing state. When the dependency is unavailable, the service continues to operate with its last known state of the world. It might not have the most recent updates, but it operates the same way it did before the dependency became impaired. In Amazon EC2, all the configuration information for existing Amazon EC2 instances is stored in the data plane as a read-only copy of the control plane’s information. This allows the data plane to operate correctly even if the control plane is unavailable.

Asynchronous interaction
Services that are strongly coupled together with a dependency in a synchronous way means that if the dependency is unavailable, so is the service. If their interactions are instead asynchronous, work can be queued or delayed during temporary periods of unavailability. For example, updates from the control plane can be pushed to the data plane asynchronously so that control plane actions succeed even if there’s a transient condition that would have prevented applying the update synchronously. These types of queues need to be bounded so the service doesn’t create an insurmountable queue.

 These patterns help make sure that even if the ability to create, modify, or delete resources is impaired, existing resources remain available. Static stability is a concept that’s deeply ingrained in how AWS designs its services, but it’s also a pattern that you can use. Design your application to operate statically during failure and avoid control plane dependencies for recovery. For more details on static stability, control planes, and data planes, see the Amazon Builders’ Library article [Static stability using Availability Zones](https://builder.aws.com/content/3K9SiqiJ369TGkkGzqPM95BuYWI/static-stability-using-availability-zones).
