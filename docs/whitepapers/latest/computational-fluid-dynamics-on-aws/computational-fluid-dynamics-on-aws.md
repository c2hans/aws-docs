---
source_url: https://docs.aws.amazon.com/whitepapers/latest/computational-fluid-dynamics-on-aws/computational-fluid-dynamics-on-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Computational Fluid Dynamics on AWS
<a name="computational-fluid-dynamics-on-aws"></a>

Publication date: **March 24, 2022** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 The scalable nature and variable demand of computational fluid dynamics (CFD) workloads makes them well suited for a cloud computing environment. This whitepaper describes best practices for running CFD workloads on Amazon Web Services (AWS). Use this document to learn more about AWS services, and the related quick start tools that simplify getting started with running CFD cases on AWS.

## Introduction
<a name="introduction"></a>

 Fluid dynamics is the study of the motion of fluids, usually in the presence of an object. Typical fluid flows of interest to engineers and scientist include flow in pipes, through engines, and around objects, such as buildings, automobiles, and airplanes. Computational fluid dynamics (CFD) is the study of these flows using a numerical approach. CFD involves the solution of conservation equations (mass, momentum, energy, and others) in a finite domain.

 Many CFD tools are currently available, including specialized and *in-house* tools. This variety is the result of the broad domain of physical problems solved with CFD. There is not a universal code for all applications, although there are packages that offer great capabilities. Broad CFD capabilities are available in commercial packages, such as ANSYS Fluent, Siemens Simcenter STAR-CCM\+, Metacomp Technologies CFD\+\+, and open-source packages, such as OpenFOAM and SU2.

 A typical CFD simulation involves the following four steps:
+  **Define the geometry** — In some cases, this step is simple, such as modeling flow in a duct. In other cases, this step involves complex components and moving parts, such as modeling a gas turbine engine. For many cases, the geometry creation is extremely time-consuming. The geometry step is graphics intensive and requires a capable graphics workstation, preferably with a Graphics Processing Unit (GPU). Often, the geometry is provided by a designer, but the CFD engineer must “clean” the geometry for input into the flow solver or mesh generation tool. This can be a tedious and time-consuming step and can sometimes require a large amount of system memory (RAM) depending on the complexity of the geometry.
+  **Generate the mesh or grid** — Mesh generation is a critical step because computational accuracy is dependent on the size, cell location, and skewness or orthogonality of the cells. In the following figure, a hybrid mesh is shown on a slice through an aircraft wing. Mesh generation can be iterative with the solution, where fixes to the mesh are driven by an understanding of flow features and gradients in the solution. Meshing is frequently an interactive process and its elliptical nature generally requires a substantial amount of memory. Like geometry definition, generating a single mesh can take hours, days, weeks, and sometimes months. Many mesh generation codes are still limited to a single node, so general-purpose [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2) instances, such as the M family, or memory-optimized instances, such as the R family, are often used.

![A diagram depicting mesh generation.](https://docs.aws.amazon.com/whitepapers/latest/computational-fluid-dynamics-on-aws/images/mesh-generation.jpeg)

+  **Solve for the solution** — This step is the primary focus of this whitepaper. For some solutions, tens of thousands of cores (processors) run over weeks to achieve a solution. Conversely, some jobs may run in just minutes when scaled out appropriately.

   There are choices for model equations depending on the desired solution fidelity. The [Navier-Stokes equations](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_equations) form the basis of the solved equations for most fluid calculations. The addition of chemical reactions, liquid and gas multi-phase flows, and many other physical properties create increasing complexity. For example, increasing the fidelity of turbulence modeling is achieved with various approximate equation sets such as Reynolds Average Navier-Stokes (RANS), Large Eddy Simulation (LES), Delayed Detached Eddy Simulation (DDES), and Direct Numerical Simulation (DNS). These approaches typically do not change the fundamental computational characteristics or scaling of the simulation.
+  **Post process through visualization** — Examples of this step include the creation of images, video, and post processing of flow fields, such as creating total forces and moments. Similar to the geometry and mesh steps, this can be graphics and memory intensive, and graphics processing units (GPUs) are often favored.

![A diagram depicting post-processing visualization.](https://docs.aws.amazon.com/whitepapers/latest/computational-fluid-dynamics-on-aws/images/post-processing-visualization.png)
