from .base import Base


class Channels(Base):

    def get_all_channels(self, params=None):
        """Get a list of all channels

        not_associated_to_group: A group id to exclude channels that are associated with that group via GroupChannel records. This can also be left blank with ``not_associated_to_group=``.
        page: The page to select.
        per_page: The number of channels per page.
        exclude_default_channels: Whether to exclude default channels (ex Town Square, Off-Topic) from the results.
        include_deleted: Include channels that have been archived. This correlates to the ``DeleteAt`` flag being set in the database.
        include_total_count: Appends a total count of returned channels inside the response object - ex: ``{ "channels": [], "total_count" : 0 }``.
        exclude_policy_constrained: If set to true, channels which are part of a data retention policy will be excluded. The ``sysconsole_read_compliance`` permission is required to use this parameter.
        *Minimum server version*: 5.35

        `Read in Mattermost API docs (channels - GetAllChannels) <https://api.mattermost.com/#tag/channels/operation/GetAllChannels>`_

        """
        return self.client.get("""/api/v4/channels""", params=params)

    def create_channel(self, options):
        """Create a channel

        team_id: The team ID of the team to create the channel on
        name: The unique handle for the channel, will be present in the channel URL
        display_name: The non-unique UI name for the channel
        purpose: A short description of the purpose of the channel
        header: Markdown-formatted text to display in the header of the channel
        type: 'O' for a public channel, 'P' for a private channel

        `Read in Mattermost API docs (channels - CreateChannel) <https://api.mattermost.com/#tag/channels/operation/CreateChannel>`_

        """
        return self.client.post("""/api/v4/channels""", options=options)

    def create_direct_channel(self, options):
        """Create a direct message channel
        `Read in Mattermost API docs (channels - CreateDirectChannel) <https://api.mattermost.com/#tag/channels/operation/CreateDirectChannel>`_

        """
        return self.client.post("""/api/v4/channels/direct""", options=options)

    def create_group_channel(self, options):
        """Create a group message channel
        `Read in Mattermost API docs (channels - CreateGroupChannel) <https://api.mattermost.com/#tag/channels/operation/CreateGroupChannel>`_

        """
        return self.client.post("""/api/v4/channels/group""", options=options)

    def search_all_channels(self, options):
        """Search all private and open type channels across all teams

        term: The string to search in the channel name, display name, and purpose.
        not_associated_to_group: A group id to exclude channels that are associated to that group via GroupChannel records.
        exclude_default_channels: Exclude default channels from the results by setting this parameter to true.
        team_ids: Filters results to channels belonging to the given team ids

        *Minimum server version*: 5.26

        group_constrained: Filters results to only return channels constrained to a group

        *Minimum server version*: 5.26

        exclude_group_constrained: Filters results to exclude channels constrained to a group

        *Minimum server version*: 5.26

        public: Filters results to only return Public / Open channels, can be used in conjunction with ``private`` to return both ``public`` and ``private`` channels

        *Minimum server version*: 5.26

        private: Filters results to only return Private channels, can be used in conjunction with ``public`` to return both ``private`` and ``public`` channels

        *Minimum server version*: 5.26

        deleted: Filters results to only return deleted / archived channels

        *Minimum server version*: 5.26

        page: The page number to return, if paginated. If this parameter is not present with the ``per_page`` parameter then the results will be returned un-paged.
        per_page: The number of entries to return per page, if paginated. If this parameter is not present with the ``page`` parameter then the results will be returned un-paged.
        exclude_policy_constrained: If set to true, only channels which do not have a granular retention policy assigned to them will be returned. The ``sysconsole_read_compliance_data_retention`` permission is required to use this parameter.
        *Minimum server version*: 5.35

        include_search_by_id: If set to true, returns channels where given search 'term' matches channel ID.
        *Minimum server version*: 5.35


        `Read in Mattermost API docs (channels - SearchAllChannels) <https://api.mattermost.com/#tag/channels/operation/SearchAllChannels>`_

        """
        return self.client.post("""/api/v4/channels/search""", options=options)

    def search_group_channels(self, options):
        """Search Group Channels

        term: The search term to match against the members' usernames of the group channels

        `Read in Mattermost API docs (channels - SearchGroupChannels) <https://api.mattermost.com/#tag/channels/operation/SearchGroupChannels>`_

        """
        return self.client.post("""/api/v4/channels/group/search""", options=options)

    def get_public_channels_by_ids_for_team(self, team_id, options):
        """Get a list of channels by ids

        team_id: Team GUID

        `Read in Mattermost API docs (channels - GetPublicChannelsByIdsForTeam) <https://api.mattermost.com/#tag/channels/operation/GetPublicChannelsByIdsForTeam>`_

        """
        return self.client.post(f"/api/v4/teams/{team_id}/channels/ids", options=options)

    def get_channel_members_timezones(self, channel_id):
        """Get timezones in a channel

        channel_id: Channel GUID

        `Read in Mattermost API docs (channels - GetChannelMembersTimezones) <https://api.mattermost.com/#tag/channels/operation/GetChannelMembersTimezones>`_

        """
        return self.client.get(f"/api/v4/channels/{channel_id}/timezones")

    def get_channel(self, channel_id):
        """Get a channel

        channel_id: Channel GUID

        `Read in Mattermost API docs (channels - GetChannel) <https://api.mattermost.com/#tag/channels/operation/GetChannel>`_

        """
        return self.client.get(f"/api/v4/channels/{channel_id}")

    def update_channel(self, channel_id, options):
        """Update a channel

        channel_id: Channel GUID
        id: The channel's id, not updatable
        name: The unique handle for the channel, will be present in the channel URL
        display_name: The non-unique UI name for the channel
        purpose: A short description of the purpose of the channel
        header: Markdown-formatted text to display in the header of the channel

        `Read in Mattermost API docs (channels - UpdateChannel) <https://api.mattermost.com/#tag/channels/operation/UpdateChannel>`_

        """
        return self.client.put(f"/api/v4/channels/{channel_id}", options=options)

    def delete_channel(self, channel_id):
        """Delete a channel

        channel_id: Channel GUID

        `Read in Mattermost API docs (channels - DeleteChannel) <https://api.mattermost.com/#tag/channels/operation/DeleteChannel>`_

        """
        return self.client.delete(f"/api/v4/channels/{channel_id}")

    def patch_channel(self, channel_id, options):
        """Patch a channel

        channel_id: Channel GUID
        name: The unique handle for the channel, will be present in the channel URL
        display_name: The non-unique UI name for the channel
        purpose: A short description of the purpose of the channel
        header: Markdown-formatted text to display in the header of the channel

        `Read in Mattermost API docs (channels - PatchChannel) <https://api.mattermost.com/#tag/channels/operation/PatchChannel>`_

        """
        return self.client.put(f"/api/v4/channels/{channel_id}/patch", options=options)

    def update_channel_privacy(self, channel_id, options):
        """Update channel's privacy

        channel_id: Channel GUID
        privacy: Channel privacy setting: 'O' for a public channel, 'P' for a private channel

        `Read in Mattermost API docs (channels - UpdateChannelPrivacy) <https://api.mattermost.com/#tag/channels/operation/UpdateChannelPrivacy>`_

        """
        return self.client.put(f"/api/v4/channels/{channel_id}/privacy", options=options)

    def restore_channel(self, channel_id):
        """Restore a channel

        channel_id: Channel GUID

        `Read in Mattermost API docs (channels - RestoreChannel) <https://api.mattermost.com/#tag/channels/operation/RestoreChannel>`_

        """
        return self.client.post(f"/api/v4/channels/{channel_id}/restore")

    def move_channel(self, channel_id, options):
        """Move a channel

        channel_id: Channel GUID
        team_id:
        force: Remove members those are not member of target team before moving the channel.

        `Read in Mattermost API docs (channels - MoveChannel) <https://api.mattermost.com/#tag/channels/operation/MoveChannel>`_

        """
        return self.client.post(f"/api/v4/channels/{channel_id}/move", options=options)

    def get_channel_stats(self, channel_id):
        """Get channel statistics

        channel_id: Channel GUID

        `Read in Mattermost API docs (channels - GetChannelStats) <https://api.mattermost.com/#tag/channels/operation/GetChannelStats>`_

        """
        return self.client.get(f"/api/v4/channels/{channel_id}/stats")

    def get_pinned_posts(self, channel_id):
        """Get a channel's pinned posts

        channel_id: Channel GUID

        `Read in Mattermost API docs (channels - GetPinnedPosts) <https://api.mattermost.com/#tag/channels/operation/GetPinnedPosts>`_

        """
        return self.client.get(f"/api/v4/channels/{channel_id}/pinned")

    def get_public_channels_for_team(self, team_id, params=None):
        """Get public channels

        team_id: Team GUID
        page: The page to select.
        per_page: The number of public channels per page.

        `Read in Mattermost API docs (channels - GetPublicChannelsForTeam) <https://api.mattermost.com/#tag/channels/operation/GetPublicChannelsForTeam>`_

        """
        return self.client.get(f"/api/v4/teams/{team_id}/channels", params=params)

    def get_private_channels_for_team(self, team_id, params=None):
        """Get private channels

        team_id: Team GUID
        page: The page to select.
        per_page: The number of private channels per page.

        `Read in Mattermost API docs (channels - GetPrivateChannelsForTeam) <https://api.mattermost.com/#tag/channels/operation/GetPrivateChannelsForTeam>`_

        """
        return self.client.get(f"/api/v4/teams/{team_id}/channels/private", params=params)

    def get_deleted_channels_for_team(self, team_id, params=None):
        """Get deleted channels

        team_id: Team GUID
        page: The page to select.
        per_page: The number of public channels per page.

        `Read in Mattermost API docs (channels - GetDeletedChannelsForTeam) <https://api.mattermost.com/#tag/channels/operation/GetDeletedChannelsForTeam>`_

        """
        return self.client.get(f"/api/v4/teams/{team_id}/channels/deleted", params=params)

    def autocomplete_channels_for_team(self, team_id, params=None):
        """Autocomplete channels

        team_id: Team GUID
        name: Name or display name

        `Read in Mattermost API docs (channels - AutocompleteChannelsForTeam) <https://api.mattermost.com/#tag/channels/operation/AutocompleteChannelsForTeam>`_

        """
        return self.client.get(f"/api/v4/teams/{team_id}/channels/autocomplete", params=params)

    def autocomplete_channels_for_team_for_search(self, team_id, params=None):
        """Autocomplete channels for search

        team_id: Team GUID
        name: Name or display name

        `Read in Mattermost API docs (channels - AutocompleteChannelsForTeamForSearch) <https://api.mattermost.com/#tag/channels/operation/AutocompleteChannelsForTeamForSearch>`_

        """
        return self.client.get(f"/api/v4/teams/{team_id}/channels/search_autocomplete", params=params)

    def search_channels(self, team_id, options):
        """Search channels

        team_id: Team GUID
        term: The search term to match against the name or display name of channels

        `Read in Mattermost API docs (channels - SearchChannels) <https://api.mattermost.com/#tag/channels/operation/SearchChannels>`_

        """
        return self.client.post(f"/api/v4/teams/{team_id}/channels/search", options=options)

    def search_archived_channels(self, team_id, options):
        """Search archived channels

        team_id: Team GUID
        term: The search term to match against the name or display name of archived channels

        `Read in Mattermost API docs (channels - SearchArchivedChannels) <https://api.mattermost.com/#tag/channels/operation/SearchArchivedChannels>`_

        """
        return self.client.post(f"/api/v4/teams/{team_id}/channels/search_archived", options=options)

    def get_channel_by_name(self, team_id, channel_name, params=None):
        """Get a channel by name

        team_id: Team GUID
        channel_name: Channel Name
        include_deleted: Defines if deleted channels should be returned or not (Mattermost Server 5.26.0+)

        `Read in Mattermost API docs (channels - GetChannelByName) <https://api.mattermost.com/#tag/channels/operation/GetChannelByName>`_

        """
        return self.client.get(f"/api/v4/teams/{team_id}/channels/name/{channel_name}", params=params)

    def get_channel_by_name_for_team_name(self, team_name, channel_name, params=None):
        """Get a channel by name and team name

        team_name: Team Name
        channel_name: Channel Name
        include_deleted: Defines if deleted channels should be returned or not (Mattermost Server 5.26.0+)

        `Read in Mattermost API docs (channels - GetChannelByNameForTeamName) <https://api.mattermost.com/#tag/channels/operation/GetChannelByNameForTeamName>`_

        """
        return self.client.get(f"/api/v4/teams/name/{team_name}/channels/name/{channel_name}", params=params)

    def get_channel_members(self, channel_id, params=None):
        """Get channel members

        channel_id: Channel GUID
        page: The page to select.
        per_page: The number of members per page. There is a maximum limit of 200 members.

        `Read in Mattermost API docs (channels - GetChannelMembers) <https://api.mattermost.com/#tag/channels/operation/GetChannelMembers>`_

        """
        return self.client.get(f"/api/v4/channels/{channel_id}/members", params=params)

    def add_channel_member(self, channel_id, options):
        """Add user to channel

        channel_id: The channel ID
        user_id: The ID of user to add into the channel
        post_root_id: The ID of root post where link to add channel member originates

        `Read in Mattermost API docs (channels - AddChannelMember) <https://api.mattermost.com/#tag/channels/operation/AddChannelMember>`_

        """
        return self.client.post(f"/api/v4/channels/{channel_id}/members", options=options)

    def get_channel_members_by_ids(self, channel_id, options):
        """Get channel members by ids

        channel_id: Channel GUID

        `Read in Mattermost API docs (channels - GetChannelMembersByIds) <https://api.mattermost.com/#tag/channels/operation/GetChannelMembersByIds>`_

        """
        return self.client.post(f"/api/v4/channels/{channel_id}/members/ids", options=options)

    def get_channel_member(self, channel_id, user_id):
        """Get channel member

        channel_id: Channel GUID
        user_id: User GUID

        `Read in Mattermost API docs (channels - GetChannelMember) <https://api.mattermost.com/#tag/channels/operation/GetChannelMember>`_

        """
        return self.client.get(f"/api/v4/channels/{channel_id}/members/{user_id}")

    def remove_user_from_channel(self, channel_id, user_id):
        """Remove user from channel

        channel_id: Channel GUID
        user_id: User GUID

        `Read in Mattermost API docs (channels - RemoveUserFromChannel) <https://api.mattermost.com/#tag/channels/operation/RemoveUserFromChannel>`_

        """
        return self.client.delete(f"/api/v4/channels/{channel_id}/members/{user_id}")

    def update_channel_roles(self, channel_id, user_id, options):
        """Update channel roles

        channel_id: Channel GUID
        user_id: User GUID
        roles:

        `Read in Mattermost API docs (channels - UpdateChannelRoles) <https://api.mattermost.com/#tag/channels/operation/UpdateChannelRoles>`_

        """
        return self.client.put(f"/api/v4/channels/{channel_id}/members/{user_id}/roles", options=options)

    def update_channel_member_scheme_roles(self, channel_id, user_id, options):
        """Update the scheme-derived roles of a channel member.

        channel_id: Channel GUID
        user_id: User GUID
        scheme_admin:
        scheme_user:

        `Read in Mattermost API docs (channels - UpdateChannelMemberSchemeRoles) <https://api.mattermost.com/#tag/channels/operation/UpdateChannelMemberSchemeRoles>`_

        """
        return self.client.put(f"/api/v4/channels/{channel_id}/members/{user_id}/schemeRoles", options=options)

    def update_channel_notify_props(self, channel_id, user_id, options):
        """Update channel notifications

        channel_id: Channel GUID
        user_id: User GUID

        `Read in Mattermost API docs (channels - UpdateChannelNotifyProps) <https://api.mattermost.com/#tag/channels/operation/UpdateChannelNotifyProps>`_

        """
        return self.client.put(f"/api/v4/channels/{channel_id}/members/{user_id}/notify_props", options=options)

    def view_channel(self, user_id, options):
        """View channel

        user_id: User ID to perform the view action for
        channel_id: The channel ID that is being viewed. Use a blank string to indicate that all channels have lost focus.
        prev_channel_id: The channel ID of the previous channel, used when switching channels. Providing this ID will cause push notifications to clear on the channel being switched to.

        `Read in Mattermost API docs (channels - ViewChannel) <https://api.mattermost.com/#tag/channels/operation/ViewChannel>`_

        """
        return self.client.post(f"/api/v4/channels/members/{user_id}/view", options=options)

    def get_channel_members_for_user(self, user_id, team_id):
        """Get channel memberships and roles for a user

        user_id: User GUID
        team_id: Team GUID

        `Read in Mattermost API docs (channels - GetChannelMembersForUser) <https://api.mattermost.com/#tag/channels/operation/GetChannelMembersForUser>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/teams/{team_id}/channels/members")

    def get_channels_for_team_for_user(self, user_id, team_id, params=None):
        """Get channels for user

        user_id: User GUID
        team_id: Team GUID
        include_deleted: Defines if deleted channels should be returned or not
        last_delete_at: Filters the deleted channels by this time in epoch format. Does not have any effect if include_deleted is set to false.

        `Read in Mattermost API docs (channels - GetChannelsForTeamForUser) <https://api.mattermost.com/#tag/channels/operation/GetChannelsForTeamForUser>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/teams/{team_id}/channels", params=params)

    def get_channels_for_user(self, user_id, params=None):
        """Get all channels from all teams

        user_id: The ID of the user. This can also be "me" which will point to the current user.
        last_delete_at: Filters the deleted channels by this time in epoch format. Does not have any effect if include_deleted is set to false.
        include_deleted: Defines if deleted channels should be returned or not

        `Read in Mattermost API docs (channels - GetChannelsForUser) <https://api.mattermost.com/#tag/channels/operation/GetChannelsForUser>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/channels", params=params)

    def get_channel_unread(self, user_id, channel_id):
        """Get unread messages

        user_id: User GUID
        channel_id: Channel GUID

        `Read in Mattermost API docs (channels - GetChannelUnread) <https://api.mattermost.com/#tag/channels/operation/GetChannelUnread>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/channels/{channel_id}/unread")

    def update_channel_scheme(self, channel_id, options):
        """Set a channel's scheme

        channel_id: Channel GUID
        scheme_id: The ID of the scheme.

        `Read in Mattermost API docs (channels - UpdateChannelScheme) <https://api.mattermost.com/#tag/channels/operation/UpdateChannelScheme>`_

        """
        return self.client.put(f"/api/v4/channels/{channel_id}/scheme", options=options)

    def channel_members_minus_group_members(self, channel_id, params=None):
        """Channel members minus group members.

        channel_id: Channel GUID
        group_ids: A comma-separated list of group ids.
        page: The page to select.
        per_page: The number of users per page.

        `Read in Mattermost API docs (channels - ChannelMembersMinusGroupMembers) <https://api.mattermost.com/#tag/channels/operation/ChannelMembersMinusGroupMembers>`_

        """
        return self.client.get(f"/api/v4/channels/{channel_id}/members_minus_group_members", params=params)

    def get_channel_member_counts_by_group(self, channel_id, params=None):
        """Channel members counts for each group that has atleast one member in the channel

        channel_id: Channel GUID
        include_timezones: Defines if member timezone counts should be returned or not

        `Read in Mattermost API docs (channels - GetChannelMemberCountsByGroup) <https://api.mattermost.com/#tag/channels/operation/GetChannelMemberCountsByGroup>`_

        """
        return self.client.get(f"/api/v4/channels/{channel_id}/member_counts_by_group", params=params)

    def get_channel_moderations(self, channel_id):
        """Get information about channel's moderation.

        channel_id: Channel GUID

        `Read in Mattermost API docs (channels - GetChannelModerations) <https://api.mattermost.com/#tag/channels/operation/GetChannelModerations>`_

        """
        return self.client.get(f"/api/v4/channels/{channel_id}/moderations")

    def patch_channel_moderations(self, channel_id, options):
        """Update a channel's moderation settings.

        channel_id: Channel GUID

        `Read in Mattermost API docs (channels - PatchChannelModerations) <https://api.mattermost.com/#tag/channels/operation/PatchChannelModerations>`_

        """
        return self.client.put(f"/api/v4/channels/{channel_id}/moderations/patch", options=options)

    def get_sidebar_categories_for_team_for_user(self, team_id, user_id):
        """Get user's sidebar categories

        team_id: Team GUID
        user_id: User GUID

        `Read in Mattermost API docs (channels - GetSidebarCategoriesForTeamForUser) <https://api.mattermost.com/#tag/channels/operation/GetSidebarCategoriesForTeamForUser>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/teams/{team_id}/channels/categories")

    def create_sidebar_category_for_team_for_user(self, team_id, user_id, options):
        """Create user's sidebar category

        team_id: Team GUID
        user_id: User GUID

        `Read in Mattermost API docs (channels - CreateSidebarCategoryForTeamForUser) <https://api.mattermost.com/#tag/channels/operation/CreateSidebarCategoryForTeamForUser>`_

        """
        return self.client.post(f"/api/v4/users/{user_id}/teams/{team_id}/channels/categories", options=options)

    def update_sidebar_categories_for_team_for_user(self, team_id, user_id, options):
        """Update user's sidebar categories

        team_id: Team GUID
        user_id: User GUID

        `Read in Mattermost API docs (channels - UpdateSidebarCategoriesForTeamForUser) <https://api.mattermost.com/#tag/channels/operation/UpdateSidebarCategoriesForTeamForUser>`_

        """
        return self.client.put(f"/api/v4/users/{user_id}/teams/{team_id}/channels/categories", options=options)

    def get_sidebar_category_order_for_team_for_user(self, team_id, user_id):
        """Get user's sidebar category order

        team_id: Team GUID
        user_id: User GUID

        `Read in Mattermost API docs (channels - GetSidebarCategoryOrderForTeamForUser) <https://api.mattermost.com/#tag/channels/operation/GetSidebarCategoryOrderForTeamForUser>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/teams/{team_id}/channels/categories/order")

    def update_sidebar_category_order_for_team_for_user(self, team_id, user_id, options):
        """Update user's sidebar category order

        team_id: Team GUID
        user_id: User GUID

        `Read in Mattermost API docs (channels - UpdateSidebarCategoryOrderForTeamForUser) <https://api.mattermost.com/#tag/channels/operation/UpdateSidebarCategoryOrderForTeamForUser>`_

        """
        return self.client.put(f"/api/v4/users/{user_id}/teams/{team_id}/channels/categories/order", options=options)

    def get_sidebar_category_for_team_for_user(self, team_id, user_id, category_id):
        """Get sidebar category

        team_id: Team GUID
        user_id: User GUID
        category_id: Category GUID

        `Read in Mattermost API docs (channels - GetSidebarCategoryForTeamForUser) <https://api.mattermost.com/#tag/channels/operation/GetSidebarCategoryForTeamForUser>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/teams/{team_id}/channels/categories/{category_id}")

    def update_sidebar_category_for_team_for_user(self, team_id, user_id, category_id, options):
        """Update sidebar category

        team_id: Team GUID
        user_id: User GUID
        category_id: Category GUID

        `Read in Mattermost API docs (channels - UpdateSidebarCategoryForTeamForUser) <https://api.mattermost.com/#tag/channels/operation/UpdateSidebarCategoryForTeamForUser>`_

        """
        return self.client.put(
            f"/api/v4/users/{user_id}/teams/{team_id}/channels/categories/{category_id}", options=options
        )

    def remove_sidebar_category_for_team_for_user(self, team_id, user_id, category_id):
        """Delete sidebar category

        team_id: Team GUID
        user_id: User GUID
        category_id: Category GUID

        `Read in Mattermost API docs (channels - RemoveSidebarCategoryForTeamForUser) <https://api.mattermost.com/#tag/channels/operation/RemoveSidebarCategoryForTeamForUser>`_

        """
        return self.client.delete(f"/api/v4/users/{user_id}/teams/{team_id}/channels/categories/{category_id}")
