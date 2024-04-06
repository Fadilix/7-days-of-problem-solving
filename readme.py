day = input("Day : ")
problemALink = input("Problem A link : ")
problemASolution = input("A solution link : ")
problemBLink = input("Problem B link : ")
problemBSolution = input("B solution link : ")

challengeDayTemplate = f"""<tr>
      <td rowspan="2">Day {day}</td>
      <td><a href="{problemALink}">____A____</a></td>
      <td><a href="{problemASolution}">____A____</a></td>
    </tr>
    <tr>
      <td><a href="{problemBLink}">____B____</a></td>
      <td><a href="{problemBSolution}">____B____</a></td>
    </tr>"""

with open("README.md", "a") as f:
    f.write(challengeDayTemplate)
