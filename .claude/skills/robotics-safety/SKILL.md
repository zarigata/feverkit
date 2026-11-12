---
name: feverkit-robotics-safety
description: Design firmware and robot controls with hardware fail-safes.
---

# Robotics Safety

Use this skill when the task matches its purpose. Adapt to the project; it is guidance, not executable code.

1. Document voltage/current limits, pinout, motor/driver matching and mechanical constraints.
2. Include physical E-stop, current limiting, interlocks, watchdog and safe startup states.
3. Simulate before driving motors and validate with the mechanism unloaded.
4. Bound velocity, torque, travel and temperature; protect users and equipment from unexpected motion.
5. Test communication dropouts and fail-to-safe behavior independently of AI controller output.
6. Log measurements and calibration without putting credentials in firmware.

**Deliverable:** short evidence-based findings, changed files (if any), tests executed, risks, and next steps.
