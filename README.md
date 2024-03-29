# Ampyx Power AP2 Flight Data

The data set was recorded during a test flight of the Ampyx Power AP2 on 3 October 2017. It was used in [[1,2]](#References) for the validation of a fixed-wing reference model. The data was used, a.o. in [AWEBox](https://github.com/awebox/awebox/issues/65).

![](ampyx-ap2.jpg)

## Data file information

MATLAB 5.0 MAT-file, Platform: PCWIN64, Created on: Thu Jun 14 16:06:17 2018

## Data file content

The data file contains 7 data groups.

* GroundControllerInputs
* NavigationData
* ProcessedSensorData
* ServoDemandFCC
* SystemState
* WinchData
* WinchMotorData
 
Open plot_flight.py for more information on how to extract data. The complete list of variables can be found in the variables.pdf.
 
The time was recorded as [Unix time](https://en.wikipedia.org/wiki/Unix_time). The aircraft launches at time step 62775 and when converting this time to UTC we get to a launch time of 03-Oct-2017 11:23:27.

## Additional resources

A TU Delft PhD dissertation [4] was also based on dynamic simulations and flight control of the AP2. The software repository can be found in [5]. 

## Authors

* **Roland Schmehl** - *Documentation* - [GitHub](https://github.com/rschmehl)
* **Dylan Eijkelhof** - *Documentation* - [GitHub](https://github.com/DylanEij)

## License

This project is licensed under the Apache License - see the [LICENSE](LICENSE.md) file for details.

## References
[1] E.C. Malz, J. Koenemann, S. Sieberling, S. Gros: A reference model for airborne wind energy systems for optimization
and control. Renewable Energy Vol. 140, pp. 1004-1011, 2019. https://doi.org/10.1016/j.renene.2019.03.111

[2] E.C. Malz: Airborne Wind Energy - to fly or not to fly? PhD Thesis, Chalmers University of Technology, 2020. https://research.chalmers.se/en/publication/519020

[3] G. Licitra, J. Koenemann, A. Bürger, P. Williams, R. Ruiterkamp, M. Diehl: Performance assessment of a rigid wing Airborne Wind Energy pumping system. Energy Vol. 173, pp. 569-585, 2019. https://doi.org/10.1016/j.energy.2019.02.064

[4] S. Rapp: Robust Automatic Pumping Cycle Operation of Airborne Wind Energy Systems. Dissertation, TU Delft, 2021. https://doi.org/10.4233/uuid:ab2adf33-ef5d-413c-b403-2cfb4f9b6bae

[5] S. Rapp: Scripts for AWE Control Design and Simulation. Version 1. 4TU.ResearchData. software. https://doi.org/10.4121/13172666.v1

## Acknowledgments

The authors would like to express their thanks to the team of Ampyx Power for contributing this data to the research community and to Elena Malz for providing some Python source code snippets with additional explanation of the data. 
