<p align="center"><img src="https://user-images.githubusercontent.com/62266775/203602459-743170f4-3792-469a-b13f-123a8fabcaa8.png" width="220"/></p>

Easily generate sample paths of stochastic differential equations (SDEs) using the Euler-Maruyama method.
This is meant to be a tool to help understand intuitively the behaviour of sample paths of SDEs. With a little tweaking (e.g. 5000 sample paths and setting high transparency of samples in the plot) you should also be able to gauge the approximate evolution of the probability density.
The default SDEs in the code are those defining the Heston model, a typical stochastic volatility model used in mathematical finance.

![Heston](https://user-images.githubusercontent.com/62266775/203598910-ac9fa30a-5fc1-4978-9180-820c85587eb5.png)

This project serves two purposes:
- To make SDEs feel more natural to students and practitioners, by way of easily implementable examples or custom SDEs; and
- To give me a feel for software development and more programming experience in general.

There are already a few SDE samplers out there already, and I don't aim to beat them. This is a project mostly for fun, by somebody with no software development training. The project is currently in very early days. Potential directions this may go in include allowing for stochastic partial differential equation (SPDE) functionality, estimation and calibration of parameters from data, and pretty visualisation of SDEs.
