#implementation of bare sudo code

#the women that the men prefer
preferred_rankings_men = {
    'ryan': ['lizzy', 'sarah', 'zoey', 'daniella'],
    'josh': ['sarah', 'lizzy', 'daniella', 'zoey'],
    'blake': ['sarah', 'daniella', 'zoey', 'lizzy'],
    'connor': ['lizzy', 'sarah', 'zoey', 'daniella']
}

#the men that women prefer
preferred_rankings_women = {
    'lizzy': ['ryan', 'blake', 'josh', 'connor'],
    'sarah': ['ryan', 'blake', 'connor', 'josh'],
    'zoey': ['sarah', 'connor', 'ryan', 'blake'],
    'daniella': ['ryan', 'josh', 'connor', 'blake']
}

#keeps track of the people that "may" end up together
tentative_engagements = []

#men whol stil need to propose and get accepted to go the dance
free_men = []

def init_free_men():
    for man in preferred_rankings_men.keys():
        free_men.append(man)

def stable_matching():
    while(len(free_men) > 0):
        for man in free_men:
            begin_matching(man)

def begin_matching(man):
    print('DEALING WITH %s'%(man))
    for woman in preferred_rankings_men[man]:

        taken_match = [couple for couple in tentative_engagements if woman in couple]

        if (len(taken_match)==0):
            tentative_engagements.append([man, woman])
            free_men.remove(man)
            print('%s is no longer a free man and is now tentatively engaged to %s'%(man, woman))
            break
        elif (len(taken_match)>0):
            print ('%s is taken already..'%(woman))

            current_guy = preferred_rankings_women[woman].index(taken_match[0][0])
            potential_guy = preferred_rankings_women[woman].index(man)

            if (current_guy < potential_guy) :
                print('She is satisfied with %s .. '%(taken_match[0][0]))
            else:
                print('%s is better than %s'%(man, taken_match[0][0]))
                print('Making %s free again... and then tentatively accept dance between %s and %s'%(taken_match[0][0], man, woman))

                #the new gut is engaged
                #free_men.remove(man)

                #the old guy is now single
                free_men.append(taken_match[0][0])

                #update the student for the dance of the woman
                taken_match[0][0] = man
                break

def main ():
    init_free_men()
    stable_matching()

    print('COMPLETE LIST OF DANCE ACCEPTANCE\n')
    print(tentative_engagements)

if __name__ == "__main__":
    main()