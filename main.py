from fastmcp import FastMCP
import pandas as pd

mcp = FastMCP("Students Data Chatbot")

df = pd.read_csv("Students_Data.csv")

@mcp.tool()
def total_students():
    return f"Total number of students: {len(df)}"

@mcp.tool()
def average_gpa():
    return f"Average GPA: {df['GPA'].mean():.2f}"

@mcp.tool()
def students_per_department():
    counts = df['Department'].value_counts()
    return "\n".join(f"{d}: {c}" for d, c in counts.items())

@mcp.tool()
def top_gpa_students(n: int = 5):
    top = df.nlargest(n, 'GPA')[['Name', 'GPA', 'Department']]
    return top.to_string(index=False)

@mcp.tool()
def graduation_year_distribution():
    counts = df['GraduationYear'].value_counts().sort_index()
    return "\n".join(f"{y}: {c}" for y, c in counts.items())

@mcp.tool()
def average_gpa_by_department():
    avgs = df.groupby('Department')['GPA'].mean()
    return "\n".join(f"{d}: {g:.2f}" for d, g in avgs.items())

@mcp.tool()
def youngest_and_oldest():
    youngest = df.loc[df['Age'].idxmin()]
    oldest = df.loc[df['Age'].idxmax()]
    return (
        f"Youngest: {youngest['Name']} ({youngest['Age']})\n"
        f"Oldest: {oldest['Name']} ({oldest['Age']})"
    )

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)