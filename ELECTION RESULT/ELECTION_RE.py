import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    return pd.read_csv(file_path)

def calculate_results(df):
    result = df.groupby('Candidate')['Votes'].sum().reset_index()
    result = result.sort_values(by='Votes', ascending=False)
    return result

def winner(result):
    return result.iloc[0]

def regional_analysis(df):
    return df.groupby(['Region', 'Candidate'])['Votes'].sum().unstack().fillna(0)

def voter_turnout(df, total_voters):
    total_votes = df['Votes'].sum()
    turnout = (total_votes / total_voters) * 100
    return turnout

def visualize_results(result):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Votes', y='Candidate', data=result, palette='viridis')
    plt.xlabel('Total Votes')
    plt.ylabel('Candidate')
    plt.title('Election Results')
    plt.show()

def visualize_regional_analysis(region_data):
    region_data.plot(kind='bar', stacked=True, figsize=(12, 6))
    plt.title('Regional Vote Distribution')
    plt.xlabel('Region')
    plt.ylabel('Votes')
    plt.legend(title='Candidate')
    plt.show()

# Example usage
if __name__ == "__main__":
    file_path = 'election_data.csv'  
    total_voters = 500000  

    df = load_data(file_path)
    result = calculate_results(df)
    winning_candidate = winner(result)
    region_data = regional_analysis(df)
    turnout = voter_turnout(df, total_voters)

    print("Election Results:")
    print(result)
    print(f"\nWinner: {winning_candidate['Candidate']} with {winning_candidate['Votes']} votes")
    print(f"Voter Turnout: {turnout:.2f}%")
    
    visualize_results(result)
    visualize_regional_analysis(region_data)
