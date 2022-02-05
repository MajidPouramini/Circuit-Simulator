# Circuit-Simulator
Electricity Workshop Project

List of Elements:
1. bus
2. current_trans (current transformator)
3. earth
4. trans_2 (two winding transformer)
5. trans_3 (three winding transformer)
6. transmission_line
7. vlotage_supply (voltage source)
8. voltage_trans (voltage transformer)

To generate a circuit file:
1. create a json file with two properties: elements and wires
2. in elements define elements you want to use. The structure is:
    - id: a unique id for the element
    - name: the name of element (must be one the elements is the List of Elements)
    - x & y: the coordination in the board
3. in wires define the wires of your circuits. The structure has following properties:
    - from & to: the id of the elements you want to have them connected.

To run a circuit:
1. create a json file for the circuit
2. run: python main.py %relative path to your circuit file% (e.g. python main.py ./samples/circuit_1.json)
