
def busiest_stations(data, peak_time, week, which_count):
    '''
    Input (dataframe): 
    
    data: mta dataframe to be used
    
    with three conditions:
    
    peak_time: 'am' or 'pm'
    week: 'weekdays' or 'weekends'
    which_count: 'entry' or 'exit'
    
    Output (series): 
    returns busiest stations according to conditions in descending order
    '''
    import datetime
    
    if peak_time == 'am':
            
        start_time = datetime.datetime.strptime('07:00:00', '%H:%M:%S')
        start_time.time
    
        end_time = datetime.datetime.strptime('10:00:00', '%H:%M:%S')
        end_time.time

    if peak_time == 'pm':
            
        start_time = datetime.datetime.strptime('19:00:00', '%H:%M:%S')
        start_time.time
    
        end_time = datetime.datetime.strptime('22:00:00', '%H:%M:%S')
        end_time.time
        
    if week == 'weekends':
        
        condition = (data.DAY > 5)
        
    if week == 'weekdays':
        
        condition = (data.DAY < 5) & (data.DAY >= 0)

    new_data = data[condition & (data.TIME >= start_time ) & (data.TIME <= end_time )]
    
    if which_count == 'exit':
        
        new_data = new_data[(new_data.exit_diff > 0)]
        
        return new_data.groupby(new_data.STATLINE).exit_diff.sum().sort_values(ascending = False)
    
    if which_count == 'entry':
        
        new_data = new_data[(new_data.entry_diff > 0)]
            
        return new_data.groupby(new_data.STATLINE).entry_diff.sum().sort_values(ascending = False)
