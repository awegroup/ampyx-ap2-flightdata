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
 
The time was recorded as [Unix time](https://en.wikipedia.org/wiki/Unix_time). The aircraft launches at time step 62775 and when converting this time to UTC we get to a launch time of 03-Oct-2017 11:23:27.

## Detailed data variables

<a name="br1"></a>GroundControllerInputs

logData\_FCC114\_1.GroundControllerInputs.packetData.UTC\_Time
 logData\_FCC114\_1.GroundControllerInputs.packetData.DF\_telemetry logData\_FCC114\_1.GroundControllerInputs.packetData.telemetry

logData\_FCC114\_1.GroundControllerInputs.packetData.telemetry.GCC\_ControlFlags
logData\_FCC114\_1.GroundControllerInputs.packetData.telemetry.systemState
logData\_FCC114\_1.GroundControllerInputs.packetData.telemetry.trueAirspeed
logData\_FCC114\_1.GroundControllerInputs.packetData.telemetry.altitude

` `logData\_FCC114\_1.GroundControllerInputs.packetData.telemetry.altitude.value
logData\_FCC114\_1.GroundControllerInputs.packetData.telemetry.velocityPlaneGround
logData\_FCC114\_1.GroundControllerInputs.packetData.telemetry.distancePlaneGround
logData\_FCC114\_1.GroundControllerInputs.packetData.telemetry.accelerationPlaneGround
 logData\_FCC114\_1.GroundControllerInputs.packetData.telemetry.accelerationPlaneGround.va
logData\_FCC114\_1.GroundControllerInputs.packetData.telemetry.controlDemand
 logData\_FCC114\_1.GroundControllerInputs.packetData.telemetry.controlDemand.value

logData\_FCC114\_1.GroundControllerInputs.packetData.telemetryUTC\_Time
 logData\_FCC114\_1.GroundControllerInputs.packetData.DF\_GCS\_GCC\_StateCommand

logData\_FCC114\_1.GroundControllerInputs.packetData.GCS\_GCC\_StateCommand
 logData\_FCC114\_1.GroundControllerInputs.packetData.GCS\_GCC\_StateCommand.UTC\_Time
 logData\_FCC114\_1.GroundControllerInputs.packetData.GCS\_GCC\_StateCommand.commandFlag
 logData\_FCC114\_1.GroundControllerInputs.packetData.GCS\_GCC\_StateCommand.data

logData\_FCC114\_1.GroundControllerInputs.packetData.DF\_GCS\_GCC\_Command

logData\_FCC114\_1.GroundControllerInputs.packetData.GCS\_GCC\_Command
 logData\_FCC114\_1.GroundControllerInputs.packetData.GCS\_GCC\_Command.UTC\_Time
 logData\_FCC114\_1.GroundControllerInputs.packetData.GCS\_GCC\_Command.commandID
 logData\_FCC114\_1.GroundControllerInputs.packetData.GCS\_GCC\_Command.data

logData\_FCC114\_1.GroundControllerInputs.packetData.DF\_winchData

logData\_FCC114\_1.GroundControllerInputs.packetData.winchData

logData\_FCC114\_1.GroundControllerInputs.packetData.winchData.winchID
 logData\_FCC114\_1.GroundControllerInputs.packetData.winchData.state
 logData\_FCC114\_1.GroundControllerInputs.packetData.winchData.ecode
 logData\_FCC114\_1.GroundControllerInputs.packetData.winchData.alarm0
 logData\_FCC114\_1.GroundControllerInputs.packetData.winchData.alarm1
 logData\_FCC114\_1.GroundControllerInputs.packetData.winchData.alarm2
 logData\_FCC114\_1.GroundControllerInputs.packetData.winchData.speed\_demand
 logData\_FCC114\_1.GroundControllerInputs.packetData.winchData.length\_total
 logData\_FCC114\_1.GroundControllerInputs.packetData.winchData.length\_on\_drum
 logData\_FCC114\_1.GroundControllerInputs.packetData.winchData.tether\_speed
 logData\_FCC114\_1.GroundControllerInputs.packetData.winchData.tether\_tension

logData\_FCC114\_1.GroundControllerInputs.packetData.DF\_winchMotorData

logData\_FCC114\_1.GroundControllerInputs.packetData.winchMotorData

logData\_FCC114\_1.GroundControllerInputs.packetData.winchMotorData.alarms
 logData\_FCC114\_1.GroundControllerInputs.packetData.winchMotorData.dc\_voltage
 logData\_FCC114\_1.GroundControllerInputs.packetData.winchMotorData.stator\_freq
 logData\_FCC114\_1.GroundControllerInputs.packetData.winchMotorData.rms\_current
 logData\_FCC114\_1.GroundControllerInputs.packetData.winchMotorData.active\_power
 logData\_FCC114\_1.GroundControllerInputs.packetData.winchMotorData.active\_current
 logData\_FCC114\_1.GroundControllerInputs.packetData.winchMotorData.torque
 logData\_FCC114\_1.GroundControllerInputs.packetData.winchMotorData.actual\_freq
 logData\_FCC114\_1.GroundControllerInputs.packetData.winchMotorData.output\_rms\_voltage
 logData\_FCC114\_1.GroundControllerInputs.packetData.winchMotorData.error\_count

logData\_FCC114\_1.GroundControllerInputs.packetData.DF\_telemetrySync

logData\_FCC114\_1.GroundControllerInputs.packetData.telemetrySync

logData\_FCC114\_1.GroundControllerInputs.packetData.telemetrySync.systemState
 logData\_FCC114\_1.GroundControllerInputs.packetData.telemetrySync.numberOfPackets
 logData\_FCC114\_1.GroundControllerInputs.packetData.telemetrySync.packetIndex
 logData\_FCC114\_1.GroundControllerInputs.packetData.telemetrySync.syncData




<a name="br2"></a>NavigationData

logData\_FCC114\_1.NavigationData.packetData.navMode

logData\_FCC114\_1.NavigationData.packetData.UTC\_Time

logData\_FCC114\_1.NavigationData.packetData.positionLLH

logData\_FCC114\_1.NavigationData.packetData.positionNED

logData\_FCC114\_1.NavigationData.packetData.velocityNED

logData\_FCC114\_1.NavigationData.packetData.rollPitchYaw

logData\_FCC114\_1.NavigationData.packetData.bodyRate

logData\_FCC114\_1.NavigationData.packetData.navAccel

logData\_FCC114\_1.NavigationData.packetData.bodyAccel

logData\_FCC114\_1.NavigationData.packetData.inertialAccel

logData\_FCC114\_1.NavigationData.packetData.windSpeed

logData\_FCC114\_1.NavigationData.packetData.gravityNED

logData\_FCC114\_1.NavigationData.packetData.heightAboveGround

logData\_FCC114\_1.NavigationData.packetData.heightAboveGroundRate

logData\_FCC114\_1.NavigationData.packetData.terrainPitchRoll

logData\_FCC114\_1.NavigationData.packetData.angleOfAttackOffset

logData\_FCC114\_1.NavigationData.packetData.sideSlipOffset

logData\_FCC114\_1.NavigationData.packetData.cosMatBodyToNav

logData\_FCC114\_1.NavigationData.packetData.pressureAltitudeOffset

logData\_FCC114\_1.NavigationData.packetData.angularAccel



<a name="br3"></a>ProcessedSensorData

logData\_FCC114\_1.ProcessedSensorData.packetData.propulsionBatteryRemaining
 logData\_FCC114\_1.ProcessedSensorData.packetData.airDataInterfaceHealth
 logData\_FCC114\_1.ProcessedSensorData.packetData.trueAirspeed
 logData\_FCC114\_1.ProcessedSensorData.packetData.equivalentAirspeed
 logData\_FCC114\_1.ProcessedSensorData.packetData.dynamicPressure
 logData\_FCC114\_1.ProcessedSensorData.packetData.inverseDynamicPressure
 logData\_FCC114\_1.ProcessedSensorData.packetData.angleOfAttackValid
 logData\_FCC114\_1.ProcessedSensorData.packetData.angleOfAttack
 logData\_FCC114\_1.ProcessedSensorData.packetData.sideSlipValid
 logData\_FCC114\_1.ProcessedSensorData.packetData.sideSlip logData\_FCC114\_1.ProcessedSensorData.packetData.pressureAltitude
logData\_FCC114\_1.ProcessedSensorData.packetData.cableTension
logData\_FCC114\_1.ProcessedSensorData.packetData.autopilotVoltage
logData\_FCC114\_1.ProcessedSensorData.packetData.servoVoltage1
logData\_FCC114\_1.ProcessedSensorData.packetData.servoVoltage2
logData\_FCC114\_1.ProcessedSensorData.packetData.PPS\_Pulse logData\_FCC114\_1.ProcessedSensorData.packetData.highRangeAccelerometer
logData\_FCC114\_1.ProcessedSensorData.packetData.engineVoltage
logData\_FCC114\_1.ProcessedSensorData.packetData.engineCurrent
logData\_FCC114\_1.ProcessedSensorData.packetData.engineConsumption
logData\_FCC114\_1.ProcessedSensorData.packetData.engineDischarge
logData\_FCC114\_1.ProcessedSensorData.packetData.engineSwitch logData\_FCC114\_1.ProcessedSensorData.packetData.servoDeflections

logData\_FCC114\_1.ProcessedSensorData.packetData.servoDeflections.stbdFlap
 logData\_FCC114\_1.ProcessedSensorData.packetData.servoDeflections.DF\_portAileron
 logData\_FCC114\_1.ProcessedSensorData.packetData.servoDeflections.portAileron
 logData\_FCC114\_1.ProcessedSensorData.packetData.servoDeflections.DF\_stbdAileron
 logData\_FCC114\_1.ProcessedSensorData.packetData.servoDeflections.stbdAileron
 logData\_FCC114\_1.ProcessedSensorData.packetData.servoDeflections.DF\_portElevator
 logData\_FCC114\_1.ProcessedSensorData.packetData.servoDeflections.portElevator
 logData\_FCC114\_1.ProcessedSensorData.packetData.servoDeflections.DF\_stbdElevator
 logData\_FCC114\_1.ProcessedSensorData.packetData.servoDeflections.stbdElevator
 logData\_FCC114\_1.ProcessedSensorData.packetData.servoDeflections.DF\_rudder
 logData\_FCC114\_1.ProcessedSensorData.packetData.servoDeflections.rudder
 logData\_FCC114\_1.ProcessedSensorData.packetData.servoDeflections.DF\_portFlap
 logData\_FCC114\_1.ProcessedSensorData.packetData.servoDeflections.portFlap
 logData\_FCC114\_1.ProcessedSensorData.packetData.servoDeflections.DF\_stbdFlap

logData\_FCC114\_1.ProcessedSensorData.packetData.CPU\_Temperature



<a name="br4"></a>ServoDemandFCC

logData\_FCC114\_1.ServoDemandFCC.packetData.demands

` `logData\_FCC114\_1.ServoDemandFCC.packetData.demands.flags
logData\_FCC114\_1.ServoDemandFCC.packetData.demands.throttle
logData\_FCC114\_1.ServoDemandFCC.packetData.demands.port\_aileron
logData\_FCC114\_1.ServoDemandFCC.packetData.demands.stbd\_aileron
logData\_FCC114\_1.ServoDemandFCC.packetData.demands.port\_flap
logData\_FCC114\_1.ServoDemandFCC.packetData.demands.stbd\_flap
logData\_FCC114\_1.ServoDemandFCC.packetData.demands.rudder
logData\_FCC114\_1.ServoDemandFCC.packetData.demands.elevator

SystemState

logData\_FCC114\_1.SystemState.packetData.currentState

logData\_FCC114\_1.SystemState.packetData.currentSubState

logData\_FCC114\_1.SystemState.packetData.previousState

logData\_FCC114\_1.SystemState.packetData.previousSubState

logData\_FCC114\_1.SystemState.packetData.transitionTaken

logData\_FCC114\_1.SystemState.packetData.stateFlags

logData\_FCC114\_1.SystemState.packetData.commandFlags

WinchData

logData\_FCC114\_1.WinchData.packetData.winchID

logData\_FCC114\_1.WinchData.packetData.state

logData\_FCC114\_1.WinchData.packetData.ecode

logData\_FCC114\_1.WinchData.packetData.alarm0

logData\_FCC114\_1.WinchData.packetData.alarm1

logData\_FCC114\_1.WinchData.packetData.alarm2

logData\_FCC114\_1.WinchData.packetData.speed\_demand

logData\_FCC114\_1.WinchData.packetData.length\_total

logData\_FCC114\_1.WinchData.packetData.length\_on\_drum

logData\_FCC114\_1.WinchData.packetData.tether\_speed

logData\_FCC114\_1.WinchData.packetData.tether\_tension



<a name="br5"></a>WinchMotorData

logData\_FCC114\_1.WinchMotorData.packetData.alarms

logData\_FCC114\_1.WinchMotorData.packetData.dc\_voltage

logData\_FCC114\_1.WinchMotorData.packetData.stator\_freq

logData\_FCC114\_1.WinchMotorData.packetData.rms\_current

logData\_FCC114\_1.WinchMotorData.packetData.active\_power

logData\_FCC114\_1.WinchMotorData.packetData.active\_current

logData\_FCC114\_1.WinchMotorData.packetData.torque

logData\_FCC114\_1.WinchMotorData.packetData.actual\_freq

logData\_FCC114\_1.WinchMotorData.packetData.output\_rms\_voltage

logData\_FCC114\_1.WinchMotorData.packetData.error\_count


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

## Acknowledgments

The authors would like to express their thanks to the team of Ampyx Power for contributing this data to the research community and to Elena Malz for providing some Python source code snippets with additional explanation of the data. 
