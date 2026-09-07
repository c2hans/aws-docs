---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/join-a-community-race.html
---

# Join a community race
<a name="join-a-community-race"></a>

![Community races](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_races.png)

Community races allow you to test your trained DeepRacer model against other participants in competitive events organized by admins or race facilitators. When a community race is created and opened for submissions, you can select one of your trained models and submit it to the race, where it will be evaluated by running multiple laps on the designated track to record its best lap time. Your model competes against other racers' submissions, with results displayed on a leaderboard that ranks all participants based on their fastest lap times, allowing you to see how your model performs compared to others without needing to race in real-time. Community races provide an exciting way to benchmark your reinforcement learning skills, experiment with different reward functions and hyperparameters, and iterate on your models to climb the rankings throughout the competition period.

**Note**
Community races are asynchronous — models are evaluated independently as they are submitted, and you do not need to be online when your model is evaluated. For real-time racing events where all participants watch together and a facilitator controls the flow, see [Live races](live-races.md).

You can see whether there are any open races that are accepting submissions by clicking the Races tab in the left sidebar. Open races that are accepting submissions will be displayed in the **Open races** section.

 **Entering a race**

You can enter a race by clicking the blue **Enter race** button at the upper-right corner of the race detail page. Doing so will bring you to a page which will reiterate the characteristics of that race in the **Race details** section, and will ask you to select which model you would like to submit to the race under the **Choose model** section. In the model selection dropdown, you will see a list of all the models you have trained that are eligible for submission.

![Enter a race](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_enter_race.png)

To enter the race, select a model from the list of options and click **Enter race**. You will be directed back to the race details page where you will be able to see your model in the **Your submissions** tab.

 **Monitoring progress**

Races are open-format and models are evaluated as they are submitted, with the leaderboard being adjusted as each result is posted. When you first submit your model to the race, you will see its status as **Queued** in the **Your submissions** tab. Your model status will then change to **Initializing** as underlying resources are warmed up. Your model status will then change to **In progress**, indicating that your model is currently up for evaluation.

When your model finishes evaluation, its status will change to **Completed**, and you will be able to see the time it took for your model to complete the race. On the **Race leaderboard** tab, you will also be able to see your rank, time, gap to first place, and number of times your model went off track. In the panel to the left, you will see your alias, your fastest time and the name of your fastest model submitted.

 **Completed races**

Completed races are races that have happened in the past. These are defined by races whose entry windows have expired, and are now shown as **Closed**. You can view past races that have occurred on the deployment, and their characteristics at a glance from the **Completed races** section. You can click **See race details** to view the in-depth characteristics of that race and its final results via its leaderboard. You can also view any submissions that you have made to that race and the outcome of those submissions.
