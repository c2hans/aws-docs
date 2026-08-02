---
source_url: https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-use-visualization.html
---

AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Work with the application visualization
<a name="microservice-extractor-use-visualization"></a>

The **Visualization** tab displays the application nodes and dependencies in graphical format. The initial view on the **Visualization **tab is the main view. The circles represent nodes, and the arrows show dependencies and direction between nodes, incoming or outgoing. By default, no groups are created. The main view reflects any updates you make to your groupings.

## Features of the AWS Microservice Extractor for .NET visualization tool
<a name="microservice-extractor-use-visualization-features"></a>

You can perform the following tasks from the **Visualization (nodes and dependencies)** page to help you group your application nodes to extract as a smaller service.

| Task | Description |
| --- | --- |
| **Create custom groups to visualize a segmentation of the service** | You can create groups in the following ways:[See the AWS documentation website for more details](http://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-use-visualization.html)<br />Groups are indicated by dotted rectangles. You can collapse and expand groups by choosing the minimize and maximize icons in the left corner of each rectangle. Collapsing a rectangle helps to reduce visual noise as you focus on other areas of the service. |
| **View node details** | Select one or more nodes. Selected nodes are indicated by a dotted circle. Incoming and outgoing dependencies for the selected nodes are highlighted as red (outgoing) or blue (incoming). If you select more than one node, each selected node will appear as dotted, and the dependencies will be highlighted for all of the selected nodes. When you choose or right-click on a node, you can select **View node details** from the **Actions** menu. The **Node details** panel appears on the right. **Node details** include the following tabs and information for one or more selected nodes:[See the AWS documentation website for more details](http://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-use-visualization.html) |
| **Reset view** | Choose **Reset view** to reset the visualization to the original state, or as it was arranged when you first launched it. All new groups are removed, and all changes will be discarded. |
| Show dependencies | Choose Show dependencies to show or hide the incoming and outgroing dependencies between nodes. By default Show dependices is selected, and incoming and outgoing dependencies are displayed on the visualization. |
| Node filter | From the Visualization Nodes and Dependencies view, you can use the Node filter search box to change the displayed nodes in the following ways:[See the AWS documentation website for more details](http://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-use-visualization.html) |
| View options | When node filters are applied you can switch between a visualization with the filters applied or a visualization with no filters. To do this, under View options select All nodes to view the visualization with no filters or select Filtered nodes to apply your selected node filters. |
| **View ****Legend** | The **Legend** displays the meanings of the symbols in the visualization. [See the AWS documentation website for more details](http://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-use-visualization.html) |
| **View ****Group classification** | Choose **Group classification** from the bottom of the visualization to view the name, ID, and color assigned to each group in the visualization. |
| **View runtime profiling information** | You can view the number of call counts from the main view by hovering over the arrows in the visualization. |
| **Edit group name and color** | After you have created a group, you can edit the name and color of the group by choosing or right-clicking it to open the **Actions** menu, then choosing **Edit group name and color**. You can update the group name and color in the **Edit group name and color** pane that appears on the right.  |
| **Add or delete canvas (main view only)** | A canvas displays a specific layout of nodes, edges, and groups. After you onboard your application, the default canvas is automatically created. You can perform graph tasks on each canvas, such as viewing node details, rearranging nodes, or creating groups. You can also add a new canvas or delete an existing one (excluding the default canvas) by selecting the option from the **Actions** dropdown menu. |
| **Get automated groupings (main view only)** | You can get automated artificial intelligence-generated grouping recommendations by selecting one of the following options on the **Get automated groupings** pop-up:[See the AWS documentation website for more details](http://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-use-visualization.html) |

## Main visualization
<a name="microservice-extractor-use-visualization-main"></a>

After you onboard an application, Microservice Extractor displays its nodes and dependencies as a graph. No groups are created by default. You can create groups, modify them, or create new groups to associate with a functionality that guides refactoring. Use the main visualization to view your groups and prepare for extraction after creating groups in the main visualization, or after exploring recommended groupings.

Manually remove node dependencies to prepare parts of your application for extraction as smaller services. The parts are displayed as groups in the graph. Microservice Extractor can also extract API endpoints as separate services by isolating the code that underlies the API endpoints and replacing local calls with network calls. This creates a new implementation of the calling class in a new solution, while preserving the interface and original solution. You can then develop, build, and deploy the new repositories independently as services.

For more information about actions you can take from the main visualization, see [Features of the AWS Microservice Extractor for .NET visualization tool](#microservice-extractor-use-visualization-features).
