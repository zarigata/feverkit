# Recipe: AI-assisted mechatronics and ESP32

Profiles: `core,robotics`

1. Specify ESP/Arduino board, voltage domains, motor drivers, wiring and mechanical constraints.
2. Create safe-state design: E-stop, deadman switch, watchdog, current limits and motor enable gating.
3. Separate high-level LLM intent from low-level deterministic control and enforce bounded trajectories.
4. Verify hardware behavior with an unloaded actuator, then controlled loads with a human supervising.
5. Test loss of communications and sensor faults before trying unattended operation.
6. Record pinouts, safety cases and measurement evidence. Do not let agents directly energize actuators during unreviewed tests.
