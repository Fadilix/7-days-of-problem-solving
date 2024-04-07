day = input("Day : ")
with open("day7links.txt", "r") as f:
    (
        problemALink,
        problemASolution,
        problemBLink,
        problemBSolution,
        problemCLink,
        problemCSolution,
    ) = f.readlines()

challengeDayTemplate = f"""<tr>
      <td rowspan="2">Day {day}</td>
      <td><a href="{problemALink}">____A____</a></td>
      <td><a href="{problemASolution}">____A____</a></td>
    </tr>
    <tr>
      <td><a href="{problemBLink}">____B____</a></td>
      <td><a href="{problemBSolution}">____B____</a></td>
    </tr>
    <tr>
      <td><a href="{problemCLink}">____C____</a></td>
      <td><a href="{problemCSolution}">____C____</a></td>
    </tr>"""

with open("README.md", "a") as f:
    f.write(challengeDayTemplate)
