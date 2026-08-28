---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/track-design-templates.html
---

# Track design templates
<a name="track-design-templates"></a>

The following track design templates show AWS DeepRacer tracks that you can build by following the instructions presented in this section.

For all tracks, to reproduce the same color production, use the following specifications:
+ Green: PMS 3395 C
+ Orange: PMS 137 C
+ Black: PMS 432 C
+ White: CMYK 0-0-2-9

These tracks were tested with the following materials for their surfaces:
+  **Vinyl**

  The tracks were printed on 13-ounce scrim vinyl with a matte finish to reduce glare. Vinyl is typically cheaper than carpet and provides good performance. Vinyl is not as durable as carpet.
+  **Carpet**

  The tracks were printed on 8-ounce, dye-sublimated, polyester-faced carpet with latex rubberized backing. Carpet is durable and provides great performance, but is expensive.

Due to their large size, the tracks cannot be easily printed on a single piece of material. Align track lines well when connecting pieces together.

 **Topics**
+  [AWS DeepRacer A to Z Speedway (Basic) track template](#atozspeedway-basic-template)
+  [AWS DeepRacer Smile Speedway (Intermediate) track template](#smile-speedway-intermediate-template)
+  [AWS DeepRacer RL Speedway (Advanced) track template](#rl-speedway-advanced-template)
+  [AWS DeepRacer Single-turn track template](#single-turn-template)
+  [AWS DeepRacer S-curve track template](#s-curve-template)
+  [AWS DeepRacer Loop track template](#loop-template)

The AWS DeepRacer A to Z Speedway (Basic) track is the most popular physical competition track in AWS DeepRacer history. It was originally released at AWS re:Invent 2018 and has the smallest footprint of all the AWS DeepRacer physical competition tracks.

![AWS DeepRacer A to Z Speedway Basic track layout](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/buildtrack-atozspeedway-basic-layout.png)

We recommend this track for beginner events and first-time racers. With a variety of runs and straightaways, it offers a compelling challenge for both first-time and experienced racers. The AWS DeepRacer A to Z Speedway (Basic) track is a 1:1 physical reproduction of the virtual track available in the console. It provides racers the opportunity to train a model in a virtual environment and then deploy the model to a physical AWS DeepRacer device for autonomous racing on a physical track.

To print or create your own A to Z Speedway (Basic) track, download the AWS DeepRacer A to Z Speedway (Basic) [track file](https://docs.aws.amazon.com/deepracer/latest/developerguide/samples/deepracer-A-to-Z-speedway-basic.ai.zip).

The AWS DeepRacer Smile Speedway track was originally released as the AWS DeepRacer Championship 2019 track.

![AWS DeepRacer Smile Speedway Intermediate track layout](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/buildtrack-smile-speedway-intermediate-layout.png)

We recommend this intermediate track for events with experienced racers and larger physical spaces. It’s a 1:1 physical reproduction of the virtual track available in the console. It provides racers the opportunity to train a model in a virtual environment and then deploy the model to a physical AWS DeepRacer device for autonomous racing on a physical track.

To print or create your own AWS DeepRacer Smile Speedway (Intermediate) track, download the AWS DeepRacer Smile Speedway (Intermediate) [track file](https://docs.aws.amazon.com/deepracer/latest/developerguide/samples/deepracer-championship-cup-intermediate.ai.zip).

The AWS DeepRacer RL Speedway (Advanced) track (aka AWS DeepRacer Summit Speedway) was originally released for AWS DeepRacer summits in 2022 and is the longest physical track in AWS DeepRacer history.

![AWS DeepRacer RL Speedway Advanced track layout](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/buildtrack-rl-speedway-advanced-layout.png)

We recommend the AWS DeepRacer RL Speedway (Advanced) track for events with experienced racers. It offers a compelling challenge for racers who enjoy going fast on straightaways. The AWS DeepRacer RL Speedway (Advanced) track is a 1:1 physical reproduction of the virtual track available in the console. It provides the opportunity for racers to train a model in a virtual environment and then deploy the model to a physical AWS DeepRacer device for autonomous racing on a physical track.

To print or create your own AWS RL Speedway (Advanced) track, download the AWS DeepRacer RL Speedway (Advanced) [track file](https://docs.aws.amazon.com/deepracer/latest/developerguide/samples/deepracer-summit-speedway-advanced.ai.zip).

This basic track template consists of two straight track segments connected by a curved track segment. Models trained with this track should make your AWS DeepRacer vehicle drive in straight line or make turns in one direction.

![AWS DeepRacer Single-turn track template](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/buildtrack-single-turn-template.png)

The track is more complex than the single-turn track because the model needs to learn to make turns in two directions. You can easily extend the single-turn track construction instructions to this track by turning it in the opposite direction after the first turn.

![AWS DeepRacer S-curve track template](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/buildtrack-s-curve-template.png)

This regular loop track is a repeating, 90-degree, single-turn track. It requires a larger enclosing area for laying the entire track.

![AWS DeepRacer Loop track template](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/buildtrack-loop-template.png)

![AWS DeepRacer Loop track visual](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/buildtrack-loop-visual.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DeepRacer on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
