---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/wave-based-refactoring/analysis-phase.html
---

# Phase 2: Analysis
<a name="analysis-phase"></a>

The analysis phase focuses on organizing the information that's gathered during the discovery phase. The following recommendations can help you analyze your IT system's existing capabilities, so you can then decompose your IT solution into independent domains and services.

**Key focus areas**
+ Creating a business map that identifies and connects each capability's dependencies
+ Prioritizing capabilities for modernization based on the metadata that's in the capabilities matrix

## Step 1: Create a business map
<a name="create-a-business-map"></a>

Create a business map that identifies and connects each domain's and subdomain's capabilities and dependencies. It can be helpful to use a tree-like hierarchical structure that uses lines to depict dependencies. This type of graphic representation can help you see which capabilities are the most isolated, or most connected to other capabilities.

## Step 2: Analyze the capability matrix
<a name="analyze-the-capability-matrix"></a>

Create a weighted scoring model based on the metadata that you gathered in your capability matrix. Make sure that you assign higher weight values to capabilities that include the highest number of dependencies and that are the most complex. Then, practice scoring the capability matrix multiple times to make sure that the scoring accurately reflects feedback from key stakeholders.

**Key considerations**
+ A capability's dependencies (how many other capabilities rely on it) is usually the most heavily weighted score.
+ Make sure that you consider transactions and analytical reporting requirements for each capability.
+ When assigning a value to the complexity of a capability, using a simple low-to-high scale is generally effective.
+ Make sure that you look for and flag duplicate capabilities, so those duplicates can be removed during the implementation phase.
+ Use the data from the business map to migrate sets of related capabilities in combined groups.
+ Preliminary selections of AWS microservices that could replace the legacy IT system's capabilities can begin at this stage.

**Note**
The analysis phase should be an iterative process, conducted with multiple business and technology stakeholders.
